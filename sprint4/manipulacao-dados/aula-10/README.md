# 🐼 Pandas Essencial: Seleção por Índices (iloc)

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #10 Seleção por Índices"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como selecionar uma ou mais linhas (observações) e colunas de um DataFrame utilizando o método `iloc` (Index-based selection) na biblioteca Pandas.

## 📚 Tópicos Abordados

- **O Método `iloc`:** Ferramenta do Pandas utilizada para selecionar elementos do DataFrame com base puramente em seus índices numéricos (posições inteiras).
- **Seleção de Linha Única:** Como extrair uma única observação informando o seu número de índice exato (o que retorna uma _Series_).
- **Fatiamento (_Slicing_):** Como aplicar o conceito de _slicing_ do Python para resgatar múltiplas linhas sequenciais informando um intervalo (ex: de 0 a 5, onde o último número não é incluso).
- **Seleção por Lista de Índices:** Como passar uma lista específica de índices numéricos para filtrar e retornar apenas as linhas desejadas, inclusive fora de ordem.
- **Seleção de Linha e Coluna Simultaneamente:** Como usar o `iloc` para acessar o cruzamento exato entre uma linha e uma coluna específicas informando as posições numéricas de ambas separadas por vírgula.

## 💻 Exemplos de Código Prático

### 1. Selecionando uma única linha

```python
import pandas as pd

# Seleciona a linha de índice 1 (a segunda linha do DataFrame)
# Retorna uma pd.Series
linha = df.iloc[1]
```

### 2. Fatiamento (Slicing) de linhas

```python
# Retorna as linhas de índice 0 a 5 (o índice 6 não é incluso)
linhas_iniciais = df.iloc[0:6]

# Retorna as linhas de índice 10 a 15
linhas_meio = df.iloc[10:16]
```

### 3. Selecionando múltiplas linhas a partir de uma lista

```python
# Retorna um novo DataFrame apenas com as linhas de índices 1, 5, 10 e 15
df_filtrado = df.iloc[[1, 5, 10, 15]]

# A seleção respeita a ordem passada na lista!
df_fora_de_ordem = df.iloc[[5, 1, 15, 10]]
```

### 4. Selecionando uma linha e uma coluna simultaneamente

```python
# Implicitamente, as colunas também possuem índices numéricos começando de 0.
# Retorna o valor exato no cruzamento da linha 1 com a coluna 4 (quinta coluna)
valor_especifico = df.iloc[1, 4]
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #10 Seleção por Índices](https://www.youtube.com/watch?v=mW00dk5kK3E) (Canal xavecoding).
