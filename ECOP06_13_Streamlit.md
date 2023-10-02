# Aplicações com Streamlit

Streamlit é uma ferramenta excelente para criar aplicativos da web interativos e é muito fácil de aprender e usar.

Antes de iniciar a aplicação é necessário criar o ambiente virtual. Isso é uma prática recomendada para evitar conflitos entre pacotes e garantir que seu aplicativo tenha todas as dependências corretas.

Claro, vou atualizar o guia para incluir a criação de um ambiente virtual Python para isolar as bibliotecas necessárias. Isso é uma prática recomendada para evitar conflitos entre pacotes e garantir que seu aplicativo tenha todas as dependências corretas. Vamos começar:

## Passo 1: Criação do ambiente virtual

Primeiro, você deve criar um ambiente virtual Python onde as bibliotecas específicas para o seu projeto serão instaladas. Vá para o diretório onde deseja criar o ambiente virtual e execute o seguinte comando para criar um ambiente virtual com o nome "ecop06" (você pode escolher outro nome se preferir):

```bash
python -m venv ecop06
```

Agora, ative o ambiente virtual:

- No Windows:

```bash
ecop06\Scripts\activate
```

- No macOS e Linux:

```bash
source ecop06/bin/activate
```

## Passo 2: Instalação do Streamlit e outras bibliotecas

Agora que você está dentro do ambiente virtual, pode instalar o Streamlit e outras bibliotecas necessárias sem afetar o ambiente global. Use o `pip` para fazer isso:

```bash
pip install streamlit pandas matplotlib
```

Esses comandos instalarão o Streamlit, o Pandas e o Matplotlib no ambiente virtual.

## Passo 3: Crie um arquivo Python para o seu aplicativo

Crie um arquivo Python (por exemplo, `app.py`) e abra-o em seu editor de código preferido.

## Passo 4: Importe as bibliotecas necessárias

Importe as bibliotecas que você precisará para o seu aplicativo. Dependendo do seu projeto, isso pode incluir bibliotecas como Pandas, Numpy e outras. Certifique-se de fazer isso dentro do ambiente virtual criado anteriormente.

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
```

## Passo 5: Crie a estrutura básica do aplicativo

Em seguida, você pode começar a criar a estrutura básica do seu aplicativo dentro do ambiente virtual:

```python
st.title("Aplicação de Controle e Automação")
```

## Passo 6: Adicione elementos à sua aplicação

Você pode adicionar vários elementos à sua aplicação, como botões, caixas de texto, gráficos e muito mais. Aqui estão alguns exemplos:

- **Botões**: Use a função `st.button` para criar botões interativos.

```python
if st.button("Clique em mim"):
    st.write("Você clicou no botão!")
```

- **Caixas de texto**: Use a função `st.text_input` para capturar entrada de texto do usuário.

```python
user_input = st.text_input("Digite algo:")
st.write("Você digitou:", user_input)
```

- **Gráficos**: Use bibliotecas como Matplotlib ou Seaborn para criar gráficos e exibi-los em seu aplicativo.

```python
import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5]
plt.plot(data)
st.pyplot()
```

## Passo 7: Execute o aplicativo

Para executar o aplicativo, vá para o terminal (ainda dentro do ambiente virtual) e navegue até o diretório onde seu arquivo `app.py` está localizado. Em seguida, execute o seguinte comando:

```bash
streamlit run app.py
```

Isso abrirá seu aplicativo no navegador padrão.

Lembre-se de que o uso de um ambiente virtual é importante para manter as dependências do projeto isoladas de outros projetos e do ambiente global do Python. Isso ajuda a garantir que seu aplicativo funcione de maneira consistente e evita conflitos de pacotes.

# Proposta

Construa um sistema monitoramento de um hospital com a montagem de gráficos baseados na base de dados abaixo:

https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/blood_pressure.csv

Permita que uma entrada de dados selecione o grupo de pacientes por faixa de idade e gênero.
