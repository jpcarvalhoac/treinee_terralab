# 🐼 Pandas Essencial: Filtragem (Parte 2) - Método Query e Reset de Índices

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #15 Filtragem (Parte 2)"** do canal xavecoding.

## 🎯 Objetivo

Apresentar uma alternativa mais legível para filtragem de dados usando o método `query`, além de demonstrar como redefinir e organizar os índices de um DataFrame após ele ser filtrado.

## 📚 Tópicos Abordados

- **O Método `query`:** Como utilizar esse método para realizar filtragens passando a condição inteira como uma única string (ex: `'estado == "SAO PAULO"'`). Isso torna o código mais limpo e similar a consultas SQL.
- **Gerenciamento de Aspas:** A regra vital de alternar entre aspas simples e duplas quando usamos o `query`. Se a string externa (a _query_) usa aspas simples `''`, qualquer string interna (o valor comparado) deve usar aspas duplas `""`, e vice-versa.
- **Boas Práticas no Armazenamento:** A importância de salvar o DataFrame filtrado em uma nova variável (ex: `df_filtrado = df.query(...)`) para evitar retrabalho e facilitar análises posteriores exclusivas àquele subconjunto de dados.
- **O Problema dos Índices Filtrados:** Após uma filtragem, o Pandas mantém os números de índices originais das linhas que sobraram (ex: 23, 45, 102...).
- **Resetando Índices (`reset_index`):** Como usar o método `reset_index()` para refazer a contagem dos índices a partir do 0 no novo DataFrame filtrado.
- **Descartando Índices Antigos (`drop=True`):** A utilização do parâmetro `drop=True` dentro do `reset_index()` para impedir que os índices antigos virem uma nova coluna inútil no DataFrame.
- **Modificação _In Place_ ou Encadeamento:** Como aplicar o reset diretamente na variável usando `inplace=True`, ou encadear a filtragem e o reset na mesma linha.

## 💻 Exemplos de Código Prático

### 1. Filtrando usando o método `query`

```python
import pandas as pd

# Utiliza aspas simples para a string do query, e aspas duplas para o valor de texto buscado
df_sao_paulo = df.query('estado == "SAO PAULO"')
```

### 2. Resetando os Índices Pós-Filtro (In Place)

```python
# df_sao_paulo herdou os índices antigos (ex: [23, 40, 89...])
# O reset_index reorganiza para [0, 1, 2...]
# drop=True evita que os índices [23, 40, 89...] virem uma nova coluna chamada 'index'
df_sao_paulo.reset_index(drop=True, inplace=True)
```

### 3. Encadeamento (Prática Comum e Elegante)

```python
# Realiza a filtragem e já reseta os índices na mesma linha (sem necessidade de inplace)
df_sao_paulo_direto = df.query('estado == "SAO PAULO"').reset_index(drop=True)
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #15 Filtragem (Parte 2)](https://www.youtube.com/watch?v=mFRYHDosxyM) (Canal xavecoding).
