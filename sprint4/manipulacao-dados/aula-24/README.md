# 🐼 Pandas Essencial: Agrupamento (Parte 2) - Múltiplos Níveis e Agregações

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #24 Agrupamento (Parte 2)"** do canal xavecoding.

## 🎯 Objetivo

Aprofundar os conhecimentos sobre o método `groupby`, demonstrando como realizar agrupamentos hierárquicos (por múltiplas colunas) e como aplicar múltiplas funções matemáticas simultaneamente usando o método de agregação (`agg`).

## 📚 Tópicos Abordados

- **Agrupamento Multinível (MultiIndex):** Como agrupar um DataFrame por mais de uma categoria sequencialmente. Basta passar uma lista de strings (nomes das colunas) para o método `groupby` (ex: agrupar primeiro por `regiao`, e dentro de cada região, agrupar por `produto`).
- **Índices Hierárquicos:** Ao realizar um agrupamento múltiplo, o Pandas gera um `MultiIndex`. Os resultados das métricas (como a média) serão apresentados em uma tabela de dupla escala.
- **Isolamento de Coluna Pós-Agrupamento:** O agrupamento processa todas as colunas numéricas por padrão. Para otimizar, o professor demonstra como selecionar uma única coluna de interesse _após_ a criação do grupo e aplicar a métrica apenas nela.
- **O Método `.agg()` (Aggregate):** Ferramenta extremamente útil para aplicar uma lista de funções (como `min`, `max`, `sum`) em um mesmo agrupamento de uma vez só, criando colunas separadas para o resultado de cada função.

## 💻 Exemplos de Código Prático

### 1. Agrupamento por Múltiplas Colunas

```python
import pandas as pd

# Agrupa primeiramente pela região e, em seguida, pelos produtos dentro de cada região
grupos_regiao_produto = df_final.groupby(['regiao', 'produto'])

# Calcula a média para os agrupamentos
# (Retornará um MultiIndex com Região -> Produto -> Médias)
medias = grupos_regiao_produto.mean()
```

### 2. Otimizando: Métrica para uma única coluna do Grupo

```python
# Em vez de calcular a média para todo o DataFrame, calcula apenas para o Preço Médio de Revenda
media_preco_revenda = grupos_regiao_produto['preco_medio_revenda'].mean()

# Você também pode aplicar o describe() apenas para esta coluna isolada
describe_preco = grupos_regiao_produto['preco_medio_revenda'].describe()
```

### 3. Agregação Múltipla com `agg()`

```python
# Cria um agrupamento simples por região
grupos_regiao = df_final.groupby('regiao')

# Para a coluna de 'preco_medio_revenda', computa o Menor (min) e o Maior (max) valor simultaneamente
# O Pandas cria uma tabela resultante com uma coluna para 'min' e outra para 'max'
min_e_max_por_regiao = grupos_regiao['preco_medio_revenda'].agg(['min', 'max'])
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #24 Agrupamento (Parte 2)](https://www.youtube.com/watch?v=kW64vySVwIM) (Canal xavecoding).
