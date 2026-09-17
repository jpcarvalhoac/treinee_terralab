# 🐼 Pandas Essencial: Estatísticas Descritivas

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #21 Estatísticas Descritivas"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como gerar e analisar estatísticas descritivas básicas de um DataFrame utilizando o Pandas, explorando tanto resumos globais quanto cálculos individuais e contagens de frequência.

## 📚 Tópicos Abordados

- **O Método `describe()`:** Uma ferramenta poderosa que calcula automaticamente diversas estatísticas (contagem, média, desvio padrão, mínimo, máximo e quartis) para todas as colunas numéricas de um DataFrame. Retorna um novo DataFrame onde as linhas são as métricas e as colunas são os atributos.
- **Filtros no `describe()`:** Como calcular estatísticas apenas para colunas específicas, seja acessando as colunas desejadas do DataFrame original antes de usar o método, ou selecionando as colunas no DataFrame resultante do `describe()`. A primeira abordagem é computacionalmente mais rápida.
- **Cálculos Individuais (`min`, `mean`, `std`):** Como calcular métricas pontuais para uma única coluna sem precisar executar o `describe()` completo, o que é útil para economizar processamento e simplificar o código.
- **Formatação de Strings Numéricas:** Dica extra de Python demonstrando como arredondar valores float para duas casas decimais utilizando `f-strings` com `: .2f`.
- **Valores Únicos e Ordenação:** Revisão do método `unique()` para listar categorias de uma coluna (ex: Estados), seguido pelo uso da função `sorted()` do Python embutida para visualizar essa lista em ordem alfabética.
- **Frequência de Dados (`value_counts()`):** Como contar a quantidade de vezes que um valor categórico aparece na base de dados (ex: quantos registros existem para cada estado). Esse método retorna uma Series ordenada de forma decrescente pela frequência, que pode ser facilmente convertida em um formato tabular usando `to_frame()`.

## 💻 Exemplos de Código Prático

### 1. Resumo Estatístico Geral com `describe()`

```python
import pandas as pd

# Gera as métricas principais para todas as colunas numéricas do dataset
estatisticas_gerais = df_final.describe()

# Otimizado: Computa as estatísticas apenas das colunas de interesse
df_focado = df_final[['preco_medio_revenda', 'preco_maximo_revenda']]
estatisticas_focadas = df_focado.describe()
```

### 2. Cálculos Individuais (Uma Coluna)

```python
# Acessando métricas isoladas diretamente da Series
valor_minimo = df_final['preco_minimo_revenda'].min()
valor_medio = df_final['preco_minimo_revenda'].mean()
desvio_padrao = df_final['preco_minimo_revenda'].std()

# Formatação de saída com f-strings (2 casas decimais)
print(f'Média: {valor_medio:.2f} +- {desvio_padrao:.2f}')
```

### 3. Valores Únicos e Ordenados

```python
# Lista todos os estados presentes na base
estados_unicos = df_final['estado'].unique()

# Retorna uma lista do Python ordenada alfabeticamente
estados_ordenados = sorted(estados_unicos)
```

### 4. Contagem de Frequência (`value_counts`)

```python
# Conta quantos registros (linhas) existem para cada estado
contagem_estados = df_final['estado'].value_counts()

# Converte a Series resultante em um DataFrame para visualização mais limpa/tabular
df_contagem = contagem_estados.to_frame()
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #21 Estatísticas Descritivas](https://www.youtube.com/watch?v=JkFEJEnmba8) (Canal xavecoding).
