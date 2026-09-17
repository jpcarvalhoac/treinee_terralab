# 🐼 Pandas Essencial: Limpeza de Dados (Parte 2) - Tratamento de Nulos

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #20 Limpeza de Dados (Parte 2)"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como identificar, analisar e tratar valores nulos (NaN) em um DataFrame, utilizando técnicas de preenchimento (`fillna`) ou remoção (`dropna`) de dados inválidos.

## 📚 Tópicos Abordados

- **Identificando Valores Nulos (`isnull()`):** Como criar uma máscara booleana para descobrir exatamente quais linhas e registros possuem dados vazios (`NaN` - Not a Number).
- **A Origem dos Nulos:** Análise de como a conversão forçada feita na aula anterior transformou "sujeiras" (como hífens `-` preenchidos no lugar de números) em valores nulos.
- **Preenchimento de Nulos (`fillna()`):** Como substituir os valores `NaN` por um valor padrão (como `0`) ou utilizar um dicionário para definir valores de preenchimento específicos para cada coluna.
- **Remoção de Nulos (`dropna()`):** Abordagem mais drástica e segura para análises precisas, excluindo do DataFrame qualquer linha (observação) que contenha ao menos um valor nulo.
- **Salvando o Dataset Final:** Após as etapas de conversão e remoção de nulos, o uso do `to_csv()` para salvar a base de dados final, limpa e padronizada.

## 💻 Exemplos de Código Prático

### 1. Criando uma máscara para encontrar valores nulos

```python
import pandas as pd

# Retorna uma Series booleana (True onde for nulo, False onde tiver dado)
mascara_nulos = df_pre['preco_medio_distribuicao'].isnull()

# Usando a máscara para visualizar os registros problemáticos
df_com_problemas = df_pre[mascara_nulos]
```

### 2. Preenchendo valores nulos (`fillna`)

```python
# Substituindo TODOS os nulos do DataFrame por 0 (retorna uma cópia)
df_preenchido = df_pre.fillna(0)

# Preenchimento personalizado por coluna usando um dicionário
valores_preenchimento = {
    'preco_medio_distribuicao': 10,
    'desvio_padrao': 20,
    'preco_minimo': 30
}
df_personalizado = df_pre.fillna(value=valores_preenchimento)
```

### 3. Removendo as linhas com valores nulos (`dropna`)

```python
# Remove qualquer linha que contenha pelo menos um valor NaN (em qualquer coluna)
# O parâmetro inplace=True aplica a alteração diretamente na variável
df_pre.dropna(inplace=True)
```

### 4. Salvando o dataset limpo

```python
# Salva o resultado final em CSV, sem gerar a coluna de índices
df_pre.to_csv('dataset_pre_processado_final.csv', index=False)
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #20 Limpeza de Dados (Parte 2)](https://www.youtube.com/watch?v=QndYAlo2Goc) (Canal xavecoding).
