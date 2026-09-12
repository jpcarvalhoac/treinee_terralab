# Pasta `geo/` — Malha Territorial do IBGE

Esta pasta é montada no container Airflow via bind mount
(`./geo:/opt/airflow/geo`, ver `docker-compose.yml` — seção "SPRINT 3") e é
onde a DAG `etl_geocoding_pipeline` procura o shapefile oficial de
municípios do IBGE, usado no filtro geográfico de UF (passo 3.2 do
desafio).

## Como popular esta pasta

1. Baixe (ou use o arquivo que você já tem) **BR_Municipios_2025.zip**,
   das Malhas Territoriais do IBGE:
   <https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html>
2. Extraia o `.zip` **diretamente dentro desta pasta** (`geo/`), de forma
   que os arquivos fiquem assim:

```
geo/
├── README.md              (este arquivo)
├── BR_Municipios_2025.shp
├── BR_Municipios_2025.shx
├── BR_Municipios_2025.dbf
├── BR_Municipios_2025.prj
├── BR_Municipios_2025.cpg
├── BR_Municipios_2025.qmd
└── LEIA-ME.txt
```

> O `.shp` completo do Brasil tem ~300 MB — por isso ele não é versionado
> no repositório (ver `.gitignore`) nem incluído no pacote entregue; cada
> ambiente deve baixá-lo/extraí-lo localmente uma vez.

## Cache dos polígonos de UF

Na primeira execução da DAG `etl_geocoding_pipeline`, a task
`filter_outside_uf` lê o shapefile completo de municípios e faz um
`dissolve` por `SIGLA_UF` para obter 1 polígono por unidade federativa —
essa operação custa ~40–50s para o Brasil inteiro. O resultado é
cacheado automaticamente em:

```
geo/uf_cache/uf_polygons.geojson
```

Nas próximas execuções, esse cache é lido diretamente (poucos segundos),
sem precisar reler/redissolver o shapefile de 300 MB. Se quiser forçar a
regeneração do cache (por exemplo, após atualizar a malha do IBGE), basta
apagar esse arquivo.
