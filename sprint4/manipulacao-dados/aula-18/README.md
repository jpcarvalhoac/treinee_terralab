# 🐼 Pandas Essencial: Filtragem (Parte 4) - Complexidade e Eficiência

Este repositório contém exemplos práticos e anotações baseados na aula **"Manipulação de Dados em Python/Pandas - #17 Filtragem (Parte 4)"** do canal xavecoding.

## 🎯 Objetivo

Aprofundar os conceitos de filtragem com múltiplas condições (Estado, Produto e Preço), comparando e demonstrando a diferença de eficiência computacional entre uma busca global e uma busca em etapas (refinamento de filtros).

## 📚 Tópicos Abordados

- **Consultas Mais Complexas:** Como estruturar uma filtragem que envolva 3 ou mais condições combinando os operadores `&` (AND) e `|` (OR).
- **Abordagem 1 - Varredura Global (Menos Eficiente):** Criação de múltiplas máscaras booleanas avaliando o DataFrame inteiro (ex: 106.000 linhas) para cada condição e cruzando os resultados lógicos no final. Funciona bem para _datasets_ pequenos, mas escala mal em termos de performance.
- **Abordagem 2 - Filtragem em Etapas (Mais Eficiente):** Técnica de refinamento sucessivo. Aplica-se a primeira condição gerando um DataFrame reduzido (ex: de 106.000 para 8.000 linhas). As condições seguintes são avaliadas apenas sobre esse DataFrame menor, poupando processamento e memória consideravelmente.
- **Checagem de Consistência (`unique()`):** O uso prático de `df['coluna'].unique()` no DataFrame já filtrado para garantir que os dados restaram apenas com as categorias solicitadas (ex: confirmar se só sobrou "SÃO PAULO" e "RIO DE JANEIRO").

## 💻 Exemplos de Código Prático

### 1. Varredura Global (Comparando o Dataset inteiro múltiplas vezes)

```python
import pandas as pd

# Avalia 106.000 linhas para cada máscara
sel_estado = (df['estado'] == 'SAO PAULO') | (df['estado'] == 'RIO DE JANEIRO')
sel_produto = df['produto'] == 'GASOLINA COMUM'
sel_preco = df['preco_medio_revenda'] > 2

# Cruza os resultados
df_final = df[sel_estado & sel_produto & sel_preco]
```

### 2. Filtragem em Etapas (Refinamento Progressivo)

```python
# Etapa 1: Filtra apenas SP e RJ (Reduz para ~8.500 linhas)
df_sp_rj = df[(df['estado'] == 'SAO PAULO') | (df['estado'] == 'RIO DE JANEIRO')]

# Etapa 2: No DataFrame reduzido, filtra apenas Gasolina (Reduz para ~1.500 linhas)
df_sp_rj_gasolina = df_sp_rj[df_sp_rj['produto'] == 'GASOLINA COMUM']

# Etapa 3: No DataFrame final, aplica a restrição de preço
df_final = df_sp_rj_gasolina[df_sp_rj_gasolina['preco_medio_revenda'] > 2]
```

### 3. Validando o Filtro com `unique()`

```python
# Verificando os valores contidos na coluna 'estado' do DataFrame final
print(df_final['estado'].unique())
# Saída esperada: ['SAO PAULO', 'RIO DE JANEIRO']

# Verificando os valores contidos na coluna 'produto'
print(df_final['produto'].unique())
# Saída esperada: ['GASOLINA COMUM']
```

## 🚀 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)

## 📺 Referência

- Vídeo da aula: [Manipulação de Dados em Python/Pandas - #17 Filtragem (Parte 4)](https://www.youtube.com/watch?v=8IXIjOV9Bpo) (Canal xavecoding).
