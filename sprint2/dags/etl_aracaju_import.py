
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional

import pandas as pd
from airflow.decorators import dag, task
from airflow.models import Variable

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuracao
# ---------------------------------------------------------------------------
# Caminho do CSV local (montado via bind mount ./data:/opt/airflow/data).
CSV_LOCAL_PATH = Variable.get(
    "aracaju_csv_path",
    default_var="/opt/airflow/data/dados_processo_seletivo.csv",
)
# Se uma URL for configurada na Variable "aracaju_csv_url", o extract faz o
# download a partir dela em vez de ler o arquivo local. Deixe em branco para
# usar o arquivo local (comportamento padrao).
CSV_URL: Optional[str] = Variable.get("aracaju_csv_url", default_var=None) or None

CITY_COLUMN = "city"
TARGET_CITY = "ARACAJU"
STAGING_TABLE = "staging_aracaju"

default_args = {
    "owner": "airflow",
    "retries": 1,
}


@dag(
    dag_id="etl_aracaju_import",
    description="Extrai o CSV de geolocalizacao, filtra municipio=Aracaju e carrega no Postgres (staging_aracaju).",
    schedule=None,  # disparo manual pela UI
    start_date=datetime(2026, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=["etl", "aracaju", "estudo-airflow"],
)
def etl_aracaju_import():
    @task
    def extract() -> str:
        """Extract: baixa (se CSV_URL estiver configurada) ou le o CSV local.

        Retorna apenas o CAMINHO do arquivo (nao os dados) para manter o
        XCom leve - o dataset completo tem 50 mil linhas.
        """
        if CSV_URL:
            import requests

            local_path = "/opt/airflow/data/_downloaded.csv"
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            logger.info("Baixando CSV de %s", CSV_URL)
            resp = requests.get(CSV_URL, timeout=60)
            resp.raise_for_status()
            with open(local_path, "wb") as f:
                f.write(resp.content)
            path = local_path
        else:
            path = CSV_LOCAL_PATH
            if not os.path.exists(path):
                raise FileNotFoundError(
                    f"CSV nao encontrado em '{path}'. Confirme o bind mount "
                    f"'./data:/opt/airflow/data' no docker-compose.yml."
                )
            logger.info("Lendo CSV local em %s", path)

        # Apenas para validar que o arquivo e legivel e logar o shape.
        df = pd.read_csv(path)
        logger.info(
            "Extract concluido: %s linhas, colunas=%s", len(df), list(df.columns)
        )
        return path

    @task
    def filter_aracaju(csv_path: str) -> List[Dict]:
        """Filter: mantem somente os registros cujo municipio seja Aracaju."""
        df = pd.read_csv(csv_path)
        total_original = len(df)

        if CITY_COLUMN not in df.columns:
            raise KeyError(
                f"Coluna '{CITY_COLUMN}' nao encontrada no CSV. "
                f"Colunas disponiveis: {list(df.columns)}"
            )

        cidade_normalizada = df[CITY_COLUMN].astype(str).str.strip().str.upper()
        df_filtrado = df[cidade_normalizada == TARGET_CITY].copy()

        if "Unnamed: 0" in df_filtrado.columns:
            df_filtrado = df_filtrado.rename(columns={"Unnamed: 0": "source_row_id"})

        # Troca NaN por None para serializacao segura via XCom (JSON).
        df_filtrado = df_filtrado.astype(object).where(df_filtrado.notna(), None)

        logger.info(
            "Filter concluido: %s de %s linhas mantidas (municipio='%s')",
            len(df_filtrado),
            total_original,
            TARGET_CITY,
        )
        if len(df_filtrado) == 0:
            logger.warning("Nenhuma linha de '%s' encontrada no CSV.", TARGET_CITY)
        if not len(df_filtrado) < total_original:
            logger.warning(
                "O total filtrado nao ficou menor que o total original - "
                "verifique o dataset de entrada."
            )

        return df_filtrado.to_dict(orient="records")

    @task
    def load(records: List[Dict]) -> None:
        """Load: grava os registros filtrados na tabela staging_aracaju no Postgres."""
        import psycopg2
        import psycopg2.extras

        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST", "postgres"),
            port=os.environ.get("POSTGRES_PORT", "5432"),
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
        )
        try:
            with conn.cursor() as cur:
                cur.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS {STAGING_TABLE} (
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
                )
                # TRUNCATE torna a task idempotente: reexecutar o DAG nao
                # duplica linhas na tabela de staging.
                cur.execute(f"TRUNCATE TABLE {STAGING_TABLE};")

                if records:
                    rows = [
                        (
                            r.get("source_row_id"),
                            r.get("city"),
                            r.get("state"),
                            r.get("latitude"),
                            r.get("longitude"),
                            r.get("accuracy"),
                            r.get("geoapi_id"),
                            r.get("date"),
                        )
                        for r in records
                    ]
                    psycopg2.extras.execute_values(
                        cur,
                        f"""
                        INSERT INTO {STAGING_TABLE}
                            (source_row_id, city, state, latitude, longitude,
                             accuracy, geoapi_id, date)
                        VALUES %s
                        """,
                        rows,
                    )
                conn.commit()

                cur.execute(f"SELECT COUNT(*) FROM {STAGING_TABLE};")
                total_staging = cur.fetchone()[0]
                cur.execute(f"SELECT DISTINCT city FROM {STAGING_TABLE};")
                cidades = [row[0] for row in cur.fetchall()]

            logger.info(
                "Load concluido: %s linha(s) gravada(s) em '%s'. Municipios presentes: %s",
                total_staging,
                STAGING_TABLE,
                cidades,
            )
        finally:
            conn.close()

    csv_path = extract()
    filtered_records = filter_aracaju(csv_path)
    load(filtered_records)


etl_aracaju_import()
