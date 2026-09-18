# 📊 Dashboards com Python: Construindo um Painel da COVID-19

Este repositório contém exemplos práticos e anotações baseados na aula **"Como construir um dashboard da COVID apenas com Python"** do canal Asimov Academy.

## 🎯 Objetivo
Aprender a construir um dashboard interativo completo para análise de dados (focado nos dados da COVID-19 no Brasil) utilizando Python, integrando ferramentas modernas de visualização de dados e layout para web.

## 📚 Tópicos Abordados

- **Bibliotecas Essenciais:** 
  - `dash`: Responsável por gerenciar o dashboard e o servidor web.
  - `dash_core_components` (dcc): Cria componentes interativos como gráficos, seletores de data e dropdowns.
  - `dash_html_components` (html): Permite a inserção de tags HTML (divs, textos, imagens) direto no Python.
  - `dash_bootstrap_components` (dbc): Facilita a criação de layouts responsivos usando o sistema de grid do Bootstrap e temas pré-configurados.
  - `plotly.express` e `plotly.graph_objects`: Ferramentas robustas para a criação de gráficos interativos (mapas cloropléticos, gráficos de barras e de linhas).
- **Tratamento de Dados (Pandas):** Leitura de arquivos `.csv` gigantes, limpeza e divisão estratégica do dataset (ex: separar dados de nível Brasil e nível Estados, descartando municípios) para otimizar o carregamento do dashboard.
- **Estruturação de Layout (Bootstrap Grid):** Uso do conceito de `Containers`, `Rows` e `Cols`. O espaço da tela é dividido em 12 partes (ex: `md=5` e `md=7`), permitindo que componentes (como o mapa e os cartões de KPIs) se ajustem de forma responsiva.
- **Criação de Mapas (Choropleth):** Utilização do arquivo `GeoJSON` para mapear os dados do dataset com as fronteiras geográficas dos estados brasileiros, colorindo-os baseado no número de casos/óbitos.
- **Interatividade com Callbacks:** O coração do Dash. Como usar o decorador `@app.callback` unindo `Inputs` (ex: clique no mapa, mudança de data no seletor) e `Outputs` (ex: atualizar o título do cartão, redesenhar o gráfico de linhas ou o mapa) para que os elementos da tela conversem entre si.
- **Loading State:** Como envolver gráficos pesados no componente `dcc.Loading` para dar um feedback visual (spinner) ao usuário enquanto os dados são processados.

## 💻 Exemplos de Código Prático

### 1. Inicializando o App e Definindo o Layout
```python
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Inicia o app já com um tema escuro do Bootstrap (CYBORG)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Estrutura básica usando Grid do Bootstrap (12 colunas no total)
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H5("Evolução COVID-19"),
            dbc.Button("BRASIL", id="location-button", color="primary", size="lg")
        ], md=5), # Ocupa 5/12 do espaço
        dbc.Col([
            dcc.Graph(id="line-graph")
        ], md=7)  # Ocupa 7/12 do espaço
    ])
], fluid=True) # fluid=True usa a tela toda
```

### 2. Tratando Dados Geográficos e Criando um Mapa Cloroplético
```python
import plotly.express as px
import json

# Lendo o arquivo GeoJSON que contém as fronteiras dos estados
with open("brasil_geo.json", "r") as f:
    brazil_states = json.load(f)

# Criando o mapa (os dados vêm do DataFrame df_states)
fig = px.choropleth_mapbox(
    df_states, 
    locations="estado",          # Coluna do DF que identifica o estado
    geojson=brazil_states,       # O arquivo de fronteiras
    color="casosNovos",          # Coluna que define a intensidade da cor
    color_continuous_scale="Redor",
    mapbox_style="carto-darkmatter", # Estilo de mapa base
    center={"lat": -16.95, "lon": -47.78}, # Centro do Brasil
    zoom=4
)
```

### 3. Criando Interatividade (Callbacks)
```python
from dash.dependencies import Input, Output

# Atualiza a variável de estado sempre que o botão ou o mapa é clicado
@app.callback(
    Output("location-button", "children"), # O que será alterado (O texto do botão)
    [Input("choropleth-map", "clickData"), # O gatilho 1 (clique no mapa)
     Input("location-button", "n_clicks")] # O gatilho 2 (clique no botão)
)
def update_location(click_data, n_clicks):
    # Lógica simplificada: Se clicou no botão, reseta para "BRASIL"
    # Se clicou no mapa, extrai o nome do estado do click_data e o retorna.
    return "BRASIL" 
```

### 4. Rodando a Aplicação
```python
# Inicializa o servidor localmente
if __name__ == "__main__":
    app.run_server(debug=True)
```

## 🚀 Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)
- [Dash](https://dash.plotly.com/)

## 📺 Referência
* Vídeo da aula: [Como construir um dashboard da COVID apenas com Python](https://www.youtube.com/watch?v=LPvchXRbstA) (Canal Asimov Academy).