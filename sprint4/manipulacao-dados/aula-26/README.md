# 🐼 Pandas Essencial: Exercícios

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #26 Exercícios"** do canal xavecoding.

## 🎯 Objetivo

Consolidar os conhecimentos adquiridos ao longo do curso resolvendo exercícios práticos com o dataset de combustíveis, unindo técnicas de filtragem, agrupamento e estatísticas descritivas para responder a perguntas de negócio.

## 📚 Tópicos Abordados

- **Filtragem de Limpeza:** Exclusão de dados incompletos (como remover o ano de 2019 da análise por não possuir os meses completos) para não enviesar os resultados.
- **Contagem por Categorias (`value_counts` com `groupby`):** Como agrupar os dados por um atributo (ex: produto) e realizar a contagem de ocorrências de outro atributo (ex: região), convertendo o resultado final em um DataFrame legível.
- **Filtragens Múltiplas e Variabilidade:** A união da função `query` (aplicando múltiplas condições com operadores lógicos) com a função `describe()` para analisar a variação (média, desvio padrão) de uma variável específica.
- **Comparação Estatística entre Grupos:** Como combinar a filtragem de múltiplos produtos (ex: Etanol e Gasolina), agrupá-los e gerar um relatório descritivo para comparar o comportamento dos preços de cada um isoladamente.
- **Próximos Passos (Estudos Futuros):** O professor encerra o curso sugerindo tópicos avançados para aprofundamento, como concatenação (`concat`), junção de tabelas (`join`/`merge`), plotagem de gráficos nativa do Pandas e análise de outliers.

## 💻 Exemplos de Código Prático

### 1. Removendo dados enviesados (Filtragem simples)

```python
import pandas as pd

# Removendo todos os registros de 2019, pois o ano não possui os 12 meses aferidos
df_valido = df[df['ano'] != 2019]
```

### 2. Quantidade de registros por Produto e Região

```python
# Agrupa pelos produtos e conta as ocorrências de cada região dentro desses grupos
contagem = df_valido.groupby('produto')['regiao'].value_counts()

# Converte a Series resultante em um DataFrame para melhor visualização
df_contagem = contagem.to_frame()
```

### 3. Filtragem Complexa com Query e Listas Externas

```python
# Definindo os produtos de interesse em uma lista
produtos_alvo = ['GASOLINA COMUM', 'ETANOL HIDRATADO']

# Consulta usando a variável externa (@produtos_alvo) e múltiplas restrições
query_str = 'produto in @produtos_alvo and estado == "SAO PAULO" and ano == 2018'
df_sp_2018 = df_valido.query(query_str)
```

### 4. Estatísticas Descritivas Comparativas

```python
# Com o DataFrame filtrado (Etanol e Gasolina em SP, 2018),
# agrupa por produto e gera as estatísticas do preço médio de revenda.
estatisticas = df_sp_2018.groupby('produto')['preco_medio_revenda'].describe()
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #26 Exercícios](https://www.youtube.com/watch?v=Fdo-71dnvOg) (Canal xavecoding).
