# 🐼 Pandas Essencial: Índices

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #09 Índices"** do canal xavecoding.

## 🎯 Objetivo
Demonstrar o conceito de índices (index) dentro de um DataFrame no Pandas, mostrando como acessá-los, convertê-los e como utilizar índices numéricos e textuais (rótulos).

## 📚 Tópicos Abordados

- **O que são Índices:** Todo DataFrame possui índices para cada linha (registro). Eles não são considerados colunas normais da tabela e servem para identificar cada observação de forma única.
- **Índices Numéricos:** Por padrão, o Pandas cria um `RangeIndex`, que é um intervalo numérico que vai de 0 até o número total de linhas menos um (0 a N-1).
- **Acessando os Índices:** Utilização do atributo `.index` para recuperar os índices atuais de um DataFrame e como convertê-los em uma lista Python usando `tolist()` ou `list()`.
- **Índices Textuais (Rótulos):** Como definir nomes/textos para os índices de um DataFrame logo no momento de sua criação, substituindo os números sequenciais por rótulos (ex: nomes de produtos).

## 💻 Exemplos de Código Prático

### 1. Acessando índices de um DataFrame existente
```python
import pandas as pd

# 'df' é um DataFrame já carregado
print(df.index) 
# Retorno comum: RangeIndex(start=0, stop=1061823, step=1)

# Convertendo os índices numéricos para uma lista comum do Python
lista_indices = df.index.tolist()
# ou
lista_indices = list(df.index)
```

### 2. Criando um DataFrame com Índices Textuais
```python
import pandas as pd

# Dados fictícios de uma pesquisa de satisfação
dados = {
    'avaliacoes_boas': [50, 45, 60],
    'avaliacoes_ruins': [10, 15, 5],
    'avaliacoes_pessimas': [2, 5, 1]
}

# Criando o DataFrame e definindo o parâmetro 'index' com rótulos textuais
df_pesquisa = pd.DataFrame(
    dados, 
    index=['Xbox', 'PlayStation 4', 'Nintendo Switch']
)

# Agora os índices são os nomes dos consoles, não 0, 1 e 2.
print(df_pesquisa.index)
# Retorno: Index(['Xbox', 'PlayStation 4', 'Nintendo Switch'], dtype='object')
```

## 🚀 Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência
* Vídeo da aula: [Manipulação de Dados em Python/Pandas - #09 Índices](https://www.youtube.com/watch?v=Mam7HmaU8d8) (Canal xavecoding).
