# 🐼 Pandas Essencial: Seleção de Colunas/Atributos

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #12 Seleção de Colunas/Atributos"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar as diferentes formas de selecionar e extrair colunas (atributos) de um DataFrame utilizando a biblioteca Pandas em Python, consolidando os métodos de acesso abordados.

## 📚 Tópicos Abordados

- **Seleção com Colchetes (Padrão):** O uso clássico passando o nome da coluna como string dentro de colchetes, que funciona para qualquer tipo de rótulo.
- **Seleção via Atributo (Ponto):** A possibilidade de acessar uma coluna como se fosse um atributo direto do objeto DataFrame (ex: `df.coluna`).
- **Restrições da Seleção via Atributo:** O acesso utilizando o ponto (`.`) **não funciona** se o nome da coluna contiver espaços, acentos, cedilha ou caracteres especiais. Nesses casos, o acesso via colchetes com string torna-se obrigatório.
- **Seleção com `loc`:** Como utilizar o método `loc` para trazer todas as linhas (usando `:`) e especificar apenas a coluna desejada.
- **Múltiplas Colunas:** Como passar uma lista contendo diversos rótulos de colunas para realizar uma filtragem múltipla. A ordem das colunas no DataFrame resultante vai respeitar exatamente a ordem informada na lista, não a do DataFrame original.

## 💻 Exemplos de Código Prático

### 1. Selecionando uma única coluna (Padrão)

```python
import pandas as pd

# Seleciona a coluna 'estado' e retorna uma pd.Series
serie_estado = df['estado']
```

### 2. Selecionando via Atributo (Notação de Ponto)

```python
# Funciona perfeitamente para nomes simples (sem espaços ou caracteres especiais)
serie_estado = df.estado
```

### 3. Exceção com Caracteres Especiais e Espaços

```python
# ERRO (SyntaxError): df.data Inicial (O Python não reconhece o espaço)
# OBRIGATÓRIO usar colchetes nesse cenário:
coluna_com_espaco = df['data Inicial']
```

### 4. Selecionando usando o `loc`

```python
# Retorna todas as linhas (:) referentes à coluna 'estado'
serie_estado_loc = df.loc[:, 'estado']
```

### 5. Selecionando múltiplas colunas simultaneamente

```python
# Passando uma lista de rótulos.
# O novo DataFrame será estruturado na ordem: produto -> estado -> regiao
df_filtrado = df[['produto', 'estado', 'regiao']]
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #12 Seleção de Colunas/Atributos](https://www.youtube.com/watch?v=9CyoJs0Tr-E) (Canal xavecoding).
