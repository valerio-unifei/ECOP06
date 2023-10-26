# Web Scraping
Web scraping é uma técnica de coleta de dados usada para extrair informações de sites da web. Isso é feito de maneira automatizada, por meio de programas de computador (ou scripts) que acessam páginas da web, fazem o download do seu conteúdo e extraem os dados desejados. Esses dados podem incluir texto, imagens, links, informações de produtos, preços, classificações, notícias e muito mais.

O processo de web scraping envolve normalmente os seguintes passos:
1. Acesso à página web: Um programa de web scraping faz uma solicitação a um servidor web para acessar uma página da web específica.
2. Download de conteúdo: O programa faz o download do conteúdo HTML da página da web. O HTML é a linguagem de marcação usada para criar páginas da web e contém todas as informações estruturadas da página.
3. Análise do HTML: O programa analisa o HTML para identificar os elementos da página que contêm os dados desejados, como tags HTML, classes CSS ou IDs.
4. Extração de dados: Os dados relevantes são extraídos desses elementos HTML identificados. Isso pode envolver a extração de texto, links, imagens ou qualquer outro tipo de informação presente na página.
5. Armazenamento ou processamento dos dados: Os dados extraídos podem ser armazenados em um banco de dados, planilha ou outro formato de arquivo, ou então podem ser processados e usados para diversos fins, como análises, comparações, agregações ou exibição em um site ou aplicativo.

Web scraping é usado em uma variedade de aplicações, incluindo monitoramento de preços de produtos, agregação de informações para análises de mercado, coleta de dados para pesquisa acadêmica, obtenção de informações para fins jornalísticos, entre outros. 

**No entanto, é importante notar que o web scraping deve ser realizado de forma ética e respeitando os termos de uso do site alvo, uma vez que seu uso indevido pode infringir direitos autorais ou violar políticas de privacidade.**

## Crie o Ambiente Virtual
Use o guia das outras aulas aqui.

## Instalando Bibliotecas
```console
(venv): pip install requests pandas bs4 openpyxl Flask
```

## Realizando a Extração dos dados

Bibliotecas no código:
```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
```

Site vasculhado: https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&page=1

Extraíndo página do site:
```python
def ofertas(pagina:int):
    # página de ofertas do mercado livre
    URL = 'https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&page=' + str(pagina)
    response = requests.get(URL)
    doc = BeautifulSoup(response.text,'html.parser')
    if response.status_code != 200:
        raise Exception('Problemas na URL: {0}'.format(response))
    # nome do produto
    produtos_tags = doc.find_all('p', class_ = 'promotion-item__title')
    for tags in produtos_tags:
        produtos.append(tags.text)
    # preço do produto
    valor_tags = doc.find_all('div', class_ = 'andes-money-amount-combo__main-container')
    for tags in valor_tags:
        valores.append(tags.text.replace('Â',''))
```

Processando extração de múltiplas páginas:
```python
for p in range(1,11):
    print('Extraindo página', p)
    ofertas(p)

ml = pd.DataFrame({
    'Produtos': produtos,
    'Preços': valores,
})

ml['Preços'] = ml['Preços'].str.extract(r'(\d+[\.,]?\d*)')

ml.to_csv('mercadolivre.csv',index=False)
```

## Proposta
Crie um site em Flask que receba o número da página e entregue uma tabela com as ofertas ordenadas de forma crescente por valor.
