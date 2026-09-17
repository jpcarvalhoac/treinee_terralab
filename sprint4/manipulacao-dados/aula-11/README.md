# 🐼 Pandas Essencial: Seleção por Labels (loc)

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #11 Seleção por Labels"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como selecionar e filtrar linhas e colunas de um DataFrame utilizando o método `loc` (Label-based selection), além de contrastá-lo com o método `iloc`.

## 📚 Tópicos Abordados

- **O Método `loc`:** Ferramenta do Pandas utilizada para acessar registros baseando-se em seus **rótulos** (labels/textos) explícitos, tanto para índices de linhas quanto para nomes de colunas.
- **Erros Comuns (`loc` vs `iloc`):** A diferença estrita de que o `iloc` espera posições numéricas inteiras, enquanto o `loc` espera o rótulo exato. Tentar cruzar essas abordagens (ex: usar um nome no `iloc` ou uma posição no `loc` para índices textuais) gera erros de chave (`KeyError` ou `TypeError`).
- **Seleção Específica (Linha e Coluna):** Como usar o `loc` passando `[rótulo_da_linha, rotulo_da_coluna]` para extrair um valor específico na interseção desejada.
- **Filtragem com Múltiplas Labels:** A possibilidade de passar uma lista de rótulos dentro do `loc` para retornar um novo DataFrame contendo apenas as linhas de interesse.
- **Uso do _Slicing_ (Fatiamento) com `:`:** Como trazer "todas as linhas" utilizando `:` e especificar apenas um subconjunto de colunas utilizando uma lista de rótulos.
- **Comportamento Dual dos Índices Numéricos:** Quando o DataFrame possui índices numéricos padrão (0, 1, 2...), o Pandas atribui implicitamente um rótulo idêntico a esses números. Nesses casos excepcionais, o `loc[1]` e o `iloc[1]` podem funcionar e retornar o mesmo registro.

## 💻 Exemplos de Código Prático

### 1. Acessando uma linha pelo seu Rótulo

```python
import pandas as pd

# Supondo 'df_pesquisa' indexado por nomes de consoles
# Retorna a linha inteira correspondente ao 'Xbox One'
linha_xbox = df_pesquisa.loc['Xbox One']
```

### 2. Acessando uma interseção exata (Linha e Coluna)

```python
# Retorna o valor exato cruzando a linha 'PlayStation 4' e a coluna 'ruim'
qtd_ruim_ps4 = df_pesquisa.loc['PlayStation 4', 'ruim']
```

### 3. Selecionando múltiplas linhas específicas

```python
# Passando uma lista de rótulos de índices
df_filtrado = df_pesquisa.loc[['Xbox One', 'Nintendo Switch']]
```

### 4. Filtrando todas as linhas e colunas específicas

```python
# O ':' indica "todas as linhas", enquanto a lista filtra as colunas
df_colunas_especificas = df_pesquisa.loc[:, ['bom', 'péssimo']]
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #11 Seleção por Labels](https://www.youtube.com/watch?v=eATaiKCw-2g) (Canal xavecoding).
