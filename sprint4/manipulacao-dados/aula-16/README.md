# 🐼 Pandas Essencial: Filtragem (Parte 3) - Múltiplas Condições

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #16 Filtragem (Parte 3)"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como realizar filtragens mais complexas no Pandas aplicando múltiplas condições lógicas (como `AND` e `OR`) simultaneamente, e discutir a eficiência de performance entre abordagens diretas e iterativas.

## 📚 Tópicos Abordados

- **Operadores Lógicos no Pandas:** Ao contrário do Python tradicional que usa `and`, `or` e `not`, o Pandas exige operadores bitwise para combinar máscaras booleanas:
  - `&` (E comercial) para **AND** (E).
  - `|` (Barra vertical) para **OR** (OU).
  - `~` (Til) para **NOT** (Negação).
- **Parênteses Obrigatórios:** Ao encadear múltiplas condições em uma mesma linha (ex: `(df['A'] == 1) & (df['B'] > 2)`), o uso de parênteses ao redor de cada condição individual é **obrigatório** devido à ordem de precedência dos operadores em Python.
- **Limitações do `query` com Caracteres Especiais:** Foi demonstrado que o método `query` não lida bem se os nomes das colunas contiverem espaços, acentos ou caracteres especiais (ex: `preço médio`), gerando erros de sintaxe (SyntaxError).
- **Problema de Ineficiência (Busca Global):** Quando aplicamos `(condição_A) & (condição_B)` no DataFrame inteiro, o Pandas varre **todas as linhas** para a Condição A, e novamente **todas as linhas** para a Condição B, o que pode ser lento em DataFrames com centenas de milhares/milhões de registros.
- **Solução Otimizada (Filtragem em Etapas):** Uma abordagem computacionalmente mais leve consiste em fazer uma filtragem por vez. Você filtra primeiro a condição mais restritiva (gerando um DataFrame muito menor) e, em seguida, aplica a segunda condição _apenas_ nesse novo DataFrame reduzido, economizando muito tempo de processamento.

## 💻 Exemplos de Código Prático

### 1. Filtragem com múltiplas condições (Abordagem Direta)

```python
import pandas as pd

# Selecionando postos do 'RIO DE JANEIRO' E com preço maior que 2
# Note a obrigatoriedade dos parênteses para separar as expressões lógicas!
selecao = (df['estado'] == 'RIO DE JANEIRO') & (df['preco_medio_revenda'] > 2)
df_filtrado = df[selecao]
```

### 2. Condição OU (OR) usando o método `query`

```python
# O método query aceita as palavras reservadas 'and' e 'or' se as colunas não tiverem acentos/espaços
df_rj_sp = df.query('estado == "RIO DE JANEIRO" or estado == "SAO PAULO"')
```

### 3. Filtragem Otimizada em Etapas (Recomendado para Grandes DataFrames)

```python
# Etapa 1: Filtra apenas RIO DE JANEIRO (reduz o DataFrame original de 106 mil para 4 mil linhas)
df_rj = df[df['estado'] == 'RIO DE JANEIRO']

# Etapa 2: Aplica a segunda condição APENAS no DataFrame já reduzido
# Muito mais rápido, pois só precisa checar a condição em 4 mil linhas, em vez de 106 mil.
df_rj_maior_2 = df_rj[df_rj['preco_medio_revenda'] > 2]
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #16 Filtragem (Parte 3)](https://www.youtube.com/watch?v=tcBwJwcWUXs) (Canal xavecoding).
