# 🐼 Pandas Essencial: Apply e Map (Mapeamento de Funções)

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #22 Apply e Map"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como aplicar e mapear funções personalizadas ou anônimas (lambda) a elementos, linhas e colunas de um DataFrame ou Series, substituindo a necessidade do lento uso de loops `for`.

## 📚 Tópicos Abordados

- **O Problema do Loop `for`:** Iterar sobre linhas de um DataFrame usando laços tradicionais (como `iterrows()`) é computacionalmente lento e desencorajado no Pandas.
- **O Método `apply`:** A principal ferramenta para mapear uma função. Ele pode ser aplicado em:
  - **Eixo 0 (`axis=0`):** Aplica a função ao longo das colunas (varre de cima para baixo).
  - **Eixo 1 (`axis=1`):** Aplica a função ao longo das linhas (varre da esquerda para a direita).
- **Funções Personalizadas e Lambdas:** Como utilizar funções tradicionais criadas com `def` ou funções anônimas (`lambda`) diretamente dentro do `apply`.
- **O Método `applymap`:** Utilizado exclusivamente em DataFrames. Diferente do `apply` (que opera sobre linhas/colunas inteiras), o `applymap` aplica a função elemento a elemento (célula por célula) de todo o DataFrame. Retorna sempre uma cópia.
- **O Método `map`:** Semelhante ao `applymap`, porém é utilizado exclusivamente para objetos do tipo `Series` (uma única coluna), aplicando a função em cada um de seus elementos individuais.
- **Dica de Performance (Métodos Nativos):** Sempre que possível, deve-se priorizar funções nativas do Pandas em vez de mapeamentos pesados. O professor exemplifica isso utilizando os métodos vetorizados de texto da classe `.str` (como `.str.upper()`) em vez de aplicar um lambda para transformar letras em maiúsculas.

## 💻 Exemplos de Código Prático

### 1. Aplicando função por Linhas usando `apply` e `axis=1`

```python
import pandas as pd

# Suponha df com colunas numéricas 'A', 'B' e 'C'
# Retorna uma Series onde cada valor é a soma dos elementos da respectiva linha
df['soma_linha'] = df.apply(lambda linha: linha['A'] + linha['B'] + linha['C'], axis=1)

# Alternativa: usando o método nativo nativo de soma (ainda melhor)
df['soma_nativa'] = df[['A', 'B', 'C']].sum(axis=1)
```

### 2. Aplicando função em Células do DataFrame usando `applymap`

```python
# Eleva ao quadrado TODOS os elementos individuais do DataFrame numérico
df_quadrado = df.applymap(lambda x: x ** 2)
```

### 3. Aplicando função em Elementos de uma Series usando `map`

```python
# Convertendo todos os nomes de uma coluna para maiúsculo
# O lambda recebe cada elemento da Series de forma isolada (x)
df['nomes_maiusculos'] = df['nome'].map(lambda x: x.upper())
```

### 4. Alternativa Nativa e Eficiente (Acessores `str`)

```python
# Uma forma muito mais otimizada e idiomática no Pandas
# para realizar a mesma transformação de texto
df['nomes_maiusculos_otimizado'] = df['nome'].str.upper()
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #22 Apply e Map](https://www.youtube.com/watch?v=PNr88Ali1b0) (Canal xavecoding).
