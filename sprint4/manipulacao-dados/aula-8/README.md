# 🐼 Pandas Essencial: Criando Colunas/Atributos

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #08 Criando Colunas/Atributos"** do canal xavecoding.

## 🎯 Objetivo
Demonstrar as diferentes formas de adicionar e manipular novas colunas (atributos) em um DataFrame utilizando a biblioteca Pandas em Python.

## 📚 Tópicos Abordados

- **Valor Constante:** Criação de uma coluna onde todas as linhas recebem o mesmo valor padrão (*default*).
- **A partir de Listas/Intervalos:** Preenchimento de uma nova coluna utilizando uma coleção de dados, como um `range()` ou lista de valores sequenciais.
- **Regras de Dimensionalidade:** A importância de garantir que o número de elementos da lista a ser inserida seja **exatamente igual** ao número de linhas do DataFrame (evitando o `ValueError`).
- **Baseado em Colunas Existentes:** Como aplicar operações matemáticas e lógicas (como a multiplicação por uma taxa de câmbio) em colunas já existentes para gerar um novo atributo.

## 💻 Exemplos de Código Prático

### 1. Criando coluna com valor constante
```python
import pandas as pd

# Supondo que 'df' seja o seu DataFrame
df['coluna_constante'] = 'valor_default'
```

### 2. Criando coluna a partir de um intervalo (range)
```python
# O range deve ter exatamente o mesmo número de linhas do DataFrame (df.shape[0])
df['coluna_por_lista'] = range(df.shape[0])
```

### 3. Criando coluna baseada em uma operação matemática
```python
# Exemplo: Multiplicando o valor da coluna 'preco_medio_reais' por 6
df['preco_em_dolar'] = df['preco_medio_reais'] * 6
```

## 🚀 Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência
* Vídeo da aula: [Manipulação de Dados em Python/Pandas - #08 Criando Colunas/Atributos](https://www.youtube.com/watch?v=ImNAoI8ooCw) (Canal xavecoding).
