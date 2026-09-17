# 🐼 Pandas Essencial: Salvando um Dataset e Removendo Colunas

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #13 Salvando um Dataset"** do canal xavecoding.

## 🎯 Objetivo

Demonstrar como limpar o DataFrame removendo colunas indesejadas e, em seguida, como exportar e salvar esse conjunto de dados processado em um arquivo CSV.

## 📚 Tópicos Abordados

- **Remoção de Colunas (`del`):** Como excluir atributos (colunas) específicos de um DataFrame usando o comando `del`. A remoção ocorre _in place_, ou seja, altera diretamente a variável na memória sem precisar criar uma cópia.
- **Limpando Ruídos:** Exemplo prático de remoção de colunas "sujas", como colunas geradas acidentalmente (ex: `Unnamed: 0`) ou colunas criadas temporariamente para testes em aulas anteriores.
- **Exportando para CSV (`to_csv`):** Utilização do método `to_csv` para salvar o DataFrame em um arquivo físico no computador.
- **Ocultando o Índice (`index=False`):** Por padrão, o Pandas salva o índice numérico (0, 1, 2...) como uma nova coluna no arquivo. O uso do parâmetro `index=False` previne esse comportamento, mantendo o arquivo mais limpo.
- **Separadores Customizados (`sep`):** Como alterar o caractere delimitador do arquivo CSV (por padrão é a vírgula `,`, mas pode ser alterado para ponto e vírgula `;`, tabulação, etc.).

## 💻 Exemplos de Código Prático

### 1. Removendo colunas indesejadas

```python
import pandas as pd

# Supondo que 'df' seja o seu DataFrame carregado
# Remove a coluna especificada in place (diretamente no df original)
del df['Unnamed: 0']
del df['coluna_sem_nocao']
```

### 2. Salvando o DataFrame em um arquivo CSV (Formato Padrão)

```python
# Salva o arquivo no diretório especificado
# Oculta o índice numérico padrão do Pandas para não virar uma coluna extra
df.to_csv('dataset_pre_processado.csv', index=False)
```

### 3. Salvando o DataFrame com um separador específico

```python
# Salva utilizando ponto e vírgula como delimitador das colunas
df.to_csv('dataset_pre_processado_ptbr.csv', index=False, sep=';')
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #13 Salvando um Dataset](https://www.youtube.com/watch?v=BA5CiN3qqI0) (Canal xavecoding).
