"""
Sprint 3 - Pipeline de qualidade de dados: fact_geocoding_clean
================================================================

Implementa os 3 passos do desafio da Sprint 3 sobre o dataset COMPLETO
(50.000 linhas, todas as UFs presentes no CSV - nao apenas Aracaju/SE
como na Sprint 2):

  3.1 Extracao       -> task `extract`
  3.2 Transformacao  -> tasks `filter_openrouteservice` e `filter_outside_uf`
  3.3 Carga          -> task `load`

Regras de transformacao (3.2):
  a) Remove linhas geocodificadas via OpenRouteService (coluna `geoapi_id`).
  b) Remove linhas cujo ponto (latitude, longitude) caia fora do poligono
     oficial da propria UF declarada na linha (coluna `state`). A checagem
     e geografica de verdade (point-in-polygon via shapely/geopandas),
     usando a Malha Municipal do IBGE (BR_Municipios_2025) fornecida pelo
     usuario - os poligonos de UF sao obtidos dissolvendo os municipios
     pela coluna SIGLA_UF.

Cada etapa de filtro loga (logger.info) quantas linhas foram removidas,
como evidencia de que a transformacao realmente rodou.

Padrao de XCom leve (mesma abordagem da Sprint 2 - `etl_aracaju_import.py`):
como o dataset completo tem 50 mil linhas (bem maior que os ~12 registros
de Aracaju da Sprint 2), as tasks NAO passam os dados inteiros pelo XCom.
Cada task de transformacao grava um CSV intermediario em disco e repassa
apenas o CAMINHO do arquivo para a proxima task.
"""

import logging
import os
from datetime import datetime
from typing import Optional

import pandas as pd
from airflow.decorators import dag, task
from airflow.models import Variable

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuracao (Airflow Variables, com defaults sensatos para rodar local)
# ---------------------------------------------------------------------------
CSV_PATH = Variable.get(
    "geocoding_csv_path",
    default_var="/opt/airflow/data/dados_processo_seletivo.csv",
)
# Shapefile da Malha Municipal do IBGE (BR_Municipios_2025), fornecido pelo
# usuario e montado via bind mount `./geo:/opt/airflow/geo` (ver docker-compose).
IBGE_MUNICIPIOS_SHP_PATH = Variable.get(
    "ibge_municipios_shp_path",
    default_var="/opt/airflow/geo/BR_Municipios_2025.shp",
)
# Cache dos poligonos de UF (dissolvidos a partir dos municipios). Gerar o
# dissolve dos 5.573 municipios custa ~40-50s; o cache evita repetir esse
# custo a cada execucao do DAG.
UF_POLYGONS_CACHE_PATH = Variable.get(
    "uf_polygons_cache_path",
    default_var="/opt/airflow/geo/uf_cache/uf_polygons.geojson",
)
INTERMEDIATE_DIR = Variable.get(
    "geocoding_intermediate_dir",
    default_var="/opt/airflow/data/_intermediate",
)
TARGET_TABLE = Variable.get(
    "geocoding_target_table",
    default_var="fact_geocoding_clean",
)

GEOAPI_COLUMN = "geoapi_id"
BLOCKED_GEOAPI = "OPENROUTESERVICE"
STATE_COLUMN = "state"
LAT_COLUMN = "latitude"
LON_COLUMN = "longitude"

default_args = {
    "owner": "airflow",
    "retries": 1,
}


# ---------------------------------------------------------------------------
# Helpers (importes pesados - geopandas/shapely - ficam dentro das funcoes
# para nao pesar o parsing do DAG pelo scheduler, mesmo padrao do
# `import psycopg2` dentro da task `load` na Sprint 2).
# ---------------------------------------------------------------------------
def _get_uf_polygons(shapefile_path: str, cache_path: str):
    """Retorna um GeoDataFrame com 1 poligono por UF (coluna SIGLA_UF).

    Se `cache_path` ja existir, le o cache (rapido, ~1-2s). Caso contrario,
    le a Malha Municipal completa do IBGE e dissolve os municipios por
    SIGLA_UF (mais custoso, ~40-50s para o Brasil inteiro), salvando o
    resultado em `cache_path` para as proximas execucoes.
    """
    import geopandas as gpd

    if os.path.exists(cache_path):
        logger.info("Lendo poligonos de UF do cache: %s", cache_path)
        return gpd.read_file(cache_path)

    if not os.path.exists(shapefile_path):
        raise FileNotFoundError(
            f"Shapefile do IBGE nao encontrado em '{shapefile_path}'. "
            f"Extraia o BR_Municipios_2025.zip (Malhas Territoriais do "
            f"IBGE) em './geo' e confirme o bind mount no docker-compose.yml."
        )

    logger.info(
        "Cache de poligonos de UF nao encontrado. Gerando a partir de "
        "'%s' (dissolve dos municipios por UF, pode levar ~1 min)...",
        shapefile_path,
    )
    municipios = gpd.read_file(shapefile_path, columns=["SIGLA_UF", "geometry"])
    uf_polygons = municipios.dissolve(by="SIGLA_UF").reset_index()
    uf_polygons = uf_polygons[["SIGLA_UF", "geometry"]]

    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    uf_polygons.to_file(cache_path, driver="GeoJSON")
    logger.info("Cache de poligonos de UF salvo em '%s'.", cache_path)
    return uf_polygons


def _remove_points_outside_uf(df: pd.DataFrame, uf_polygons) -> pd.DataFrame:
    """Mantem apenas as linhas cujo (lat, long) caia DENTRO do poligono da
    propria UF declarada na coluna `state` (point-in-polygon real, via
    geopandas/shapely). Loga o detalhamento da remocao.
    """
    import geopandas as gpd

    total_before = len(df)

    coord_mask = df[LAT_COLUMN].notna() & df[LON_COLUMN].notna()
    n_sem_coordenada = int((~coord_mask).sum())
    df_valid = df[coord_mask].copy()

    # As coordenadas do CSV sao lat/long WGS84 (EPSG:4326), padrao de APIs
    # de geocodificacao (Google/MapBox/etc). O shapefile do IBGE usa
    # SIRGAS2000 (EPSG:4674) - reprojetamos os pontos para o mesmo CRS dos
    # poligonos antes do teste point-in-polygon.
    points = gpd.GeoDataFrame(
        df_valid,
        geometry=gpd.points_from_xy(df_valid[LON_COLUMN], df_valid[LAT_COLUMN]),
        crs="EPSG:4326",
    ).to_crs(uf_polygons.crs)

    joined = gpd.sjoin(
        points,
        uf_polygons[["SIGLA_UF", "geometry"]],
        how="left",
        predicate="within",
    )
    # Salvaguarda: um ponto exatamente sobre uma fronteira poderia, em
    # teoria, casar com mais de um poligono - garante 1 linha por ponto.
    joined = joined[~joined.index.duplicated(keep="first")]

    declared_uf = joined[STATE_COLUMN].astype(str).str.strip().str.upper()
    geometric_uf = joined["SIGLA_UF"].astype(str).str.strip().str.upper()

    fora_do_brasil_mask = joined["SIGLA_UF"].isna()
    uf_divergente_mask = (~fora_do_brasil_mask) & (declared_uf != geometric_uf)
    keep_mask = (~fora_do_brasil_mask) & (declared_uf == geometric_uf)

    df_clean = joined[keep_mask].drop(
        columns=["geometry", "index_right", "SIGLA_UF"], errors="ignore"
    )

    n_fora_brasil = int(fora_do_brasil_mask.sum())
    n_uf_divergente = int(uf_divergente_mask.sum())
    n_removidos_total = n_sem_coordenada + n_fora_brasil + n_uf_divergente

    logger.info(
        "Filtro geografico (UF): %s linhas removidas de %s "
        "[sem coordenada valida=%s, fora do territorio nacional=%s, "
        "ponto geometricamente em outra UF que nao a declarada=%s]. "
        "Restaram %s linhas.",
        n_removidos_total,
        total_before,
        n_sem_coordenada,
        n_fora_brasil,
        n_uf_divergente,
        len(df_clean),
    )
    return df_clean


# ---------------------------------------------------------------------------
# DAG
# ---------------------------------------------------------------------------
@dag(
    dag_id="etl_geocoding_pipeline",
    description=(
        "Pipeline de qualidade de dados sobre o dataset completo de "
        "geolocalizacao: remove registros do OpenRouteService e pontos "
        "fora da propria UF (point-in-polygon via IBGE), carregando o "
        "resultado em fact_geocoding_clean."
    ),
    schedule=None,  # disparo manual pela UI
    start_date=datetime(2026, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=["etl", "geocoding", "qualidade-de-dados", "sprint-3"],
)
def etl_geocoding_pipeline():
    @task
    def extract() -> str:
        """3.1 Extracao: le o CSV completo e valida que e legivel.

        Retorna apenas o CAMINHO do arquivo via XCom (dataset tem 50 mil
        linhas - XCom leve, mesmo padrao da task `extract` da Sprint 2).
        """
        if not os.path.exists(CSV_PATH):
            raise FileNotFoundError(
                f"CSV nao encontrado em '{CSV_PATH}'. Confirme o bind mount "
                f"'./data:/opt/airflow/data' no docker-compose.yml."
            )
        df = pd.read_csv(CSV_PATH)
        logger.info(
            "Extract concluido: %s linhas, colunas=%s", len(df), list(df.columns)
        )
        return CSV_PATH

    @task
    def filter_openrouteservice(csv_path: str) -> str:
        """3.2a Transformacao: remove linhas geocodificadas via
        OpenRouteService (coluna `geoapi_id`).
        """
        df = pd.read_csv(csv_path)
        total_original = len(df)

        if GEOAPI_COLUMN not in df.columns:
            raise KeyError(
                f"Coluna '{GEOAPI_COLUMN}' nao encontrada no CSV. "
                f"Colunas disponiveis: {list(df.columns)}"
            )

        api_normalizada = df[GEOAPI_COLUMN].astype(str).str.strip().str.upper()
        mask_mantem = api_normalizada != BLOCKED_GEOAPI
        df_filtrado = df[mask_mantem].copy()

        removidos = total_original - len(df_filtrado)
        logger.info(
            "Filtro OpenRouteService: %s linhas removidas de %s. "
            "Distribuicao original por geoapi_id: %s. Restaram %s linhas.",
            removidos,
            total_original,
            df[GEOAPI_COLUMN].value_counts().to_dict(),
            len(df_filtrado),
        )

        os.makedirs(INTERMEDIATE_DIR, exist_ok=True)
        out_path = os.path.join(INTERMEDIATE_DIR, "step1_sem_openrouteservice.csv")
        df_filtrado.to_csv(out_path, index=False)
        return out_path

    @task
    def filter_outside_uf(csv_path: str) -> str:
        """3.2b Transformacao: remove pontos fora do poligono oficial da
        propria UF declarada em cada linha (point-in-polygon real via
        geopandas/shapely, usando a Malha Municipal do IBGE).
        """
        df = pd.read_csv(csv_path)
        uf_polygons = _get_uf_polygons(IBGE_MUNICIPIOS_SHP_PATH, UF_POLYGONS_CACHE_PATH)
        df_clean = _remove_points_outside_uf(df, uf_polygons)

        os.makedirs(INTERMEDIATE_DIR, exist_ok=True)
        out_path = os.path.join(INTERMEDIATE_DIR, "step2_dentro_da_uf.csv")
        df_clean.to_csv(out_path, index=False)
        return out_path

    @task
    def load(csv_path: str) -> None:
        """3.3 Carga: grava o DataFrame tratado em `fact_geocoding_clean`
        no PostgreSQL via SQLAlchemy. TRUNCATE + INSERT torna reruns
        idempotentes (mesmo espirito da task `load` da Sprint 2).
        """
        from sqlalchemy import create_engine, text

        df_clean = pd.read_csv(csv_path)
        if "Unnamed: 0" in df_clean.columns:
            df_clean = df_clean.rename(columns={"Unnamed: 0": "source_row_id"})
        df_clean["loaded_at"] = pd.Timestamp.utcnow()

        conn_str = (
            f"postgresql+psycopg2://{os.environ.get('POSTGRES_USER')}:"
            f"{os.environ.get('POSTGRES_PASSWORD')}@"
            f"{os.environ.get('POSTGRES_HOST', 'postgres')}:"
            f"{os.environ.get('POSTGRES_PORT', '5432')}/"
            f"{os.environ.get('POSTGRES_DB')}"
        )
        engine = create_engine(conn_str)

        create_sql = f"""
            CREATE TABLE IF NOT EXISTS {TARGET_TABLE} (
                id SERIAL PRIMARY KEY,
                source_row_id INTEGER,
                city TEXT,
                state TEXT,
                latitude DOUBLE PRECISION,
                longitude DOUBLE PRECISION,
                accuracy DOUBLE PRECISION,
                geoapi_id TEXT,
                date DATE,
                loaded_at TIMESTAMP DEFAULT now()
            );
        """
        insert_cols = [
            "source_row_id",
            "city",
            "state",
            "latitude",
            "longitude",
            "accuracy",
            "geoapi_id",
            "date",
            "loaded_at",
        ]
        df_to_insert = df_clean.reindex(columns=insert_cols)

        with engine.begin() as conn:
            conn.execute(text(create_sql))
            # Idempotencia: TRUNCATE antes do INSERT, para reexecucoes do
            # DAG nao duplicarem linhas na tabela (mesma logica da Sprint 2).
            conn.execute(text(f"TRUNCATE TABLE {TARGET_TABLE};"))

        df_to_insert.to_sql(
            TARGET_TABLE,
            engine,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=1000,
        )

        with engine.connect() as conn:
            total = conn.execute(text(f"SELECT COUNT(*) FROM {TARGET_TABLE};")).scalar()
            estados = conn.execute(
                text(f"SELECT DISTINCT state FROM {TARGET_TABLE} ORDER BY state;")
            ).fetchall()

        logger.info(
            "Load concluido: %s linha(s) gravada(s) em '%s'. UFs presentes: %s",
            total,
            TARGET_TABLE,
            [row[0] for row in estados],
        )

    csv_path = extract()
    step1_path = filter_openrouteservice(csv_path)
    step2_path = filter_outside_uf(step1_path)
    load(step2_path)


etl_geocoding_pipeline()
