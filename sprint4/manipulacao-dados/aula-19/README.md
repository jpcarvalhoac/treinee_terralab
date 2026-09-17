# 🐼 Pandas Essencial: Limpeza de Dados (Parte 1) - Conversões e Valores Nulos

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #19 Limpeza de Dados (Parte 1)"** do canal xavecoding.

## 🎯 Objetivo

Apresentar os primeiros passos para a limpeza e preparação de dados em um DataFrame, focando na identificação de tipos incorretos, criação de cópias de segurança e conversão de colunas para formatos adequados (datas e números).

## 📚 Tópicos Abordados

- **Exploração Inicial (`info()`):** Como utilizar o método `df.info()` para obter um panorama do DataFrame, verificando a quantidade de entradas, os tipos de dados inferidos pelo Pandas (ex: `int64`, `object`, `float64`) e a contagem inicial de valores não nulos.
- **Identificação de Tipos Errados:** A constatação de que colunas que deveriam ser numéricas (como preços ou margens) estavam sendo classificadas como `object` (strings). Isso geralmente indica a presença de "sujeira" (caracteres especiais, hífens ou textos) no meio dos números.
- **Cópia de Segurança (`copy()`):** A boa prática de criar um DataFrame de pré-processamento (`df_pre = df.copy()`) para realizar as limpezas, preservando o dataset original intacto na memória.
- **Conversão de Datas (`to_datetime`):** Utilização do método `pd.to_datetime()` para converter colunas de texto (que já estão em formato de data como YYYY-MM-DD) para o tipo especial `datetime64`, permitindo operações de tempo futuras.
- **Conversão Numérica (`to_numeric`):** Como usar o `pd.to_numeric()` iterando sobre uma lista de colunas para forçar a conversão de `object` para `float`/`int`.
- **Tratamento de Erros na Conversão (`errors='coerce'`):** O uso vital do parâmetro `errors='coerce'` no `to_numeric`. Se o Pandas encontrar uma string que não pode virar número (a "sujeira"), ao invés de quebrar o código (lançar uma exceção), ele substitui esse valor inválido por um nulo (`NaN` - Not a Number).

## 💻 Exemplos de Código Prático

### 1. Inspecionando o DataFrame e Criando uma Cópia

```python
import pandas as pd

# Mostra informações vitais: tipos de dados, uso de memória e valores nulos
df.info()

# Cria uma cópia isolada para o pré-processamento (boa prática)
df_pre = df.copy()
```

### 2. Convertendo Strings para Datas

```python
# Converte a coluna para o tipo datetime64
df_pre['data_inicial'] = pd.to_datetime(df_pre['data_inicial'])
```

### 3. Convertendo Strings para Numéricos e Forçando Nulos (NaN)

```python
# Lista de colunas que deveriam ser números mas estão como texto (object)
colunas_numericas = ['preco_medio', 'margem_revenda', 'desvio_padrao']

# Iterando sobre a lista para converter cada coluna
for atributo in colunas_numericas:
    # errors='coerce' transforma tudo que não for conversível em NaN (nulo)
    df_pre[atributo] = pd.to_numeric(df_pre[atributo], errors='coerce')

# Após essa operação, um novo df.info() vai revelar que valores que antes
# pareciam preenchidos (mas eram strings sujas) agora se tornaram nulos.
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #19 Limpeza de Dados (Parte 1)](https://www.youtube.com/watch?v=qKeM93NTKQM) (Canal xavecoding).
