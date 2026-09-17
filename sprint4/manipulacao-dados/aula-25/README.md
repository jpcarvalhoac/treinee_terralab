# 🐼 Pandas Essencial: Ordenação de Dados

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #25 Ordenação"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como ordenar as linhas (registros) de um DataFrame baseado nos valores de uma ou múltiplas colunas, utilizando o método `sort_values`.

## 📚 Tópicos Abordados

- **O Método `sort_values()`:** A principal função do Pandas para reordenar dados. Por padrão, ele ordena as linhas (`axis=0`) com base em uma coluna específica.
- **Ordenação Crescente e Decrescente:** O uso do parâmetro `ascending` (que por padrão é `True`). Alterá-lo para `False` inverte a ordem (do maior para o menor valor, ou de Z a A).
- **Ordenação Múltipla (Critérios de Desempate):** Como passar uma lista de colunas para realizar ordenações sequenciais. Se houver empate na primeira coluna (ex: alunos com a mesma nota), o Pandas utiliza a segunda coluna (ex: ordem alfabética do nome) para desempatar.
- **Orientação Mista (`ascending` com listas):** Ao ordenar por múltiplas colunas, é possível passar uma lista de valores booleanos para o parâmetro `ascending`, definindo uma direção (crescente ou decrescente) específica para cada coluna.
- **Alteração In Place:** O comportamento padrão do `sort_values` é retornar uma cópia ordenada do DataFrame. Para aplicar a ordenação na própria variável original, utiliza-se o parâmetro `inplace=True`.
- **Manutenção de Índices:** A ordenação embaralha a visualização dos índices originais (ex: a linha índice 3 pode ir para o topo). Relembra-se a necessidade do método `reset_index(drop=True)` se o objetivo for reconstruir a contagem de zero a N.

## 💻 Exemplos de Código Prático

### 1. Ordenação Simples (Uma Coluna)

```python
import pandas as pd

# Ordena o DataFrame baseado na coluna 'nota_final'
# Por padrão, do menor para o maior (crescente)
df_ordenado = df.sort_values(by='nota_final')

# Invertendo para ordem decrescente (maiores notas primeiro)
df_decrescente = df.sort_values(by='nota_final', ascending=False)
```

### 2. Ordenação Múltipla com Critérios de Desempate

```python
# Ordena primeiro pela 'nota_final'.
# Se a nota for igual, usa a coluna 'nome' para desempatar.
df_desempate = df.sort_values(by=['nota_final', 'nome'])
```

### 3. Ordenação com Orientações Mistas e Modificação Direta

```python
# Ordena 'nota_final' de forma decrescente (False)
# E, em caso de empate, ordena 'nome' de forma crescente/alfabética (True)
# inplace=True aplica as mudanças no próprio df, sem criar uma cópia
df.sort_values(by=['nota_final', 'nome'], ascending=[False, True], inplace=True)
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #25 Ordenação](https://www.youtube.com/watch?v=GDPMNfunNow) (Canal xavecoding).
