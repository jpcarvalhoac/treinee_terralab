# 🐼 Pandas Essencial: Filtragem (Parte 1) - Seleção Condicional

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #14 Filtragem (Parte 1)"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como realizar seleções condicionais (filtragens) em um DataFrame utilizando a biblioteca Pandas em Python, retornando apenas as linhas (observações) que atendem a um critério específico.

## 📚 Tópicos Abordados

- **Extração de Valores Únicos (`unique()`):** Como utilizar o método `unique()` em uma Series (coluna) para listar todos os valores categóricos presentes nela sem repetições. Excelente para descobrir como os dados estão escritos antes de filtrá-los.
- **Comparação Vetorizada:** Como aplicar uma condição lógica em toda uma coluna do DataFrame (ex: `df['estado'] == 'SAO PAULO'`). O resultado não é apenas um verdadeiro/falso global, mas sim uma _Series booleana_ (com o mesmo número de linhas do DataFrame) contendo `True` ou `False` para cada registro.
- **Filtragem por Colchetes (Máscara Booleana):** Como passar a _Series booleana_ (máscara) gerada pela condição lógica para dentro dos colchetes do DataFrame (`df[condicao]`). O Pandas interpretará a máscara e retornará um novo DataFrame contendo apenas as linhas onde o valor da máscara era `True`.
- **Filtragem usando `.loc`:** A alternativa de passar a mesma máscara booleana dentro do método `.loc[]`, alcançando exatamente o mesmo resultado que o método dos colchetes.

## 💻 Exemplos de Código Prático

### 1. Verificando os valores únicos de uma coluna

```python
import pandas as pd

# Retorna um array com os valores únicos (sem repetição) da coluna 'estado'
estados_unicos = df['estado'].unique()
```

### 2. Criando uma condição (Series Booleana)

```python
# Realiza uma comparação vetorial linha a linha.
# O resultado é uma Series contendo True (se for igual) ou False (se for diferente)
selecao = df['estado'] == 'SAO PAULO'

# Verificando o formato da Series gerada
print(selecao.shape) # Ex: (1061823,)
```

### 3. Aplicando a filtragem (Máscara Booleana)

```python
# O Pandas retorna um novo DataFrame apenas com as linhas onde a seleção resultou em True
df_sao_paulo = df[selecao]

# Equivalente utilizando de forma direta (mais comum e prático):
df_sao_paulo_direto = df[df['estado'] == 'SAO PAULO']
```

### 4. Filtrando usando o método `loc`

```python
# O método loc também aceita a máscara booleana para filtrar as linhas
df_sao_paulo_loc = df.loc[selecao]
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #14 Filtragem (Parte 1)](https://www.youtube.com/watch?v=eiSnlFtJOIM) (Canal xavecoding).
