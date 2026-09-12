# Airflow + PostgreSQL com Docker Compose

Ambiente local de desenvolvimento com **Apache Airflow** (`LocalExecutor`) e **PostgreSQL**, orquestrado via Docker Compose.

## Estrutura do projeto

```
.
├── dags/              # DAGs do Airflow (bind mount)
├── logs/              # Logs do Airflow (bind mount, não versionado)
├── plugins/           # Plugins do Airflow (bind mount)
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Pré-requisitos

- Docker Engine e Docker Compose Plugin instalados. Confirme com:
  ```bash
  docker --version
  docker compose version
  ```

## Como subir o ambiente localmente

1. Clone o repositório e entre na pasta:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <pasta-do-projeto>
   ```

2. Crie as pastas usadas pelo Airflow (o Git não versiona pastas vazias):
   ```bash
   mkdir -p dags logs plugins
   ```

3. Copie o arquivo de exemplo de variáveis de ambiente e ajuste os valores:
   ```bash
   cp .env.example .env
   ```
   Edite o `.env` e defina uma senha real para `POSTGRES_PASSWORD`. **Nunca** commite o `.env` real (ele já está no `.gitignore`).

4. Suba os containers em segundo plano:
   ```bash
   docker compose up -d
   ```

5. Acompanhe os logs até a inicialização terminar — na primeira subida o Airflow roda `airflow standalone`, que executa a migração do banco, cria o usuário admin e sobe scheduler + webserver, o que leva alguns minutos:
   ```bash
   docker compose logs -f airflow
   ```
   > Se o container do `airflow` sair logo no início (`Exited`), é provável que o postgres ainda não estivesse pronto para aceitar conexões. Basta rodar `docker compose up -d` novamente.

6. Pegue a senha de admin gerada automaticamente pelo `airflow standalone` (o usuário é sempre `admin`):
   ```bash
   docker exec -it airflow cat /opt/airflow/standalone_admin_password.txt
   ```

7. Acesse a interface do Airflow em [http://localhost:8080](http://localhost:8080) e faça login com usuário `admin` e a senha obtida no passo anterior.

## Parar o ambiente

```bash
docker compose down
```

## Parar e apagar os dados do Postgres (reset total)

```bash
docker compose down -v
```

## Serviços

- **postgres**: banco de dados usado como metastore do Airflow, porta `5432` exposta. Os dados são persistidos no volume nomeado `postgres_data`, sobrevivendo a restarts dos containers.
- **airflow**: roda `airflow standalone` (migração do banco + criação do usuário admin + scheduler + webserver com `LocalExecutor`), expondo a UI na porta `8080`. As pastas `dags/`, `logs/` e `plugins/` são montadas via bind mount para facilitar o desenvolvimento local.

## Variáveis de ambiente

Veja `.env.example` para a lista completa de variáveis necessárias (usadas apenas pelo serviço `postgres`). As credenciais de acesso à UI do Airflow são geradas automaticamente pelo `airflow standalone` — veja o passo 6 acima.
