# 🐼 Pandas Essencial: Agrupamento (Parte 1)

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #23 Agrupamento (Parte 1)"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar a importância e o uso do método `groupby` no Pandas para dividir um DataFrame em grupos (com base em dados categóricos) e aplicar funções estatísticas de forma independente para cada categoria.

## 📚 Tópicos Abordados

- **O que é Agrupamento:** A necessidade de analisar dados divididos por categorias (ex: regiões, estados, marcas) sem precisar criar dezenas de DataFrames filtrados manualmente.
- **O Método `groupby()`:** A função nativa do Pandas que separa as observações (linhas) baseando-se nos valores de uma coluna específica, retornando um objeto especial do tipo `DataFrameGroupBy`.
- **Atributos de Grupo:**
  - `.groups`: Retorna um dicionário onde a chave é o nome da categoria e o valor é a lista dos índices das linhas que pertencem àquela categoria.
  - `.get_group('Nome_do_Grupo')`: Retorna um DataFrame completo contendo apenas as observações (linhas) do grupo especificado.
- **Aplicando Estatísticas em Grupos:** Como calcular medidas como `.mean()`, `.min()` e `.describe()` diretamente no objeto `groupby`. O Pandas computará essas métricas de maneira segregada (uma para cada grupo), facilitando comparações.
- **Encadeamento (Chaining):** A prática comum (e mais fluida) de aplicar a função `groupby` e logo em seguida invocar o cálculo da métrica na mesma linha de código (ex: `df.groupby('coluna').mean()`).

## 💻 Exemplos de Código Prático

### 1. Criando um Agrupamento Simples

```python
import pandas as pd

# Agrupa todas as linhas do DataFrame com base na coluna 'regiao'
# Retorna um objeto DataFrameGroupBy (não é um DataFrame comum)
grupos_regiao = df_final.groupby('regiao')
```

### 2. Inspecionando e Acessando os Grupos

```python
# Retorna um dicionário com os índices de cada grupo { 'CENTRO OESTE': [1, 2, 5...], 'NORTE': [...] }
indices_dos_grupos = grupos_regiao.groups

# Retorna um DataFrame contendo APENAS as linhas da região 'CENTRO OESTE'
df_centro_oeste = grupos_regiao.get_group('CENTRO OESTE')
```

### 3. Computando Estatísticas por Grupo

```python
# Calcula a MÉDIA de todas as colunas numéricas, separadamente para cada região
media_por_regiao = grupos_regiao.mean()

# Calcula o MENOR valor de todas as colunas numéricas para cada região
minimo_por_regiao = grupos_regiao.min()

# Gera um relatório estatístico completo (contagem, média, min, max, quartis) por região
# Observação: Retornará um DataFrame com muitas colunas
describe_por_regiao = grupos_regiao.describe()
```

### 4. Boas Práticas (Encadeamento de Métodos)

```python
# Cria o grupo e já calcula a média na mesma linha (muito comum no dia a dia)
medias = df_final.groupby('regiao').mean()
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #23 Agrupamento (Parte 1)](https://www.youtube.com/watch?v=YSrQfO94KUY) (Canal xavecoding).
