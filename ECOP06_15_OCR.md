# Criando Aplicação com OCR
Aprender a montar um OCR (Optical Character Recognition) online com Python oferece várias vantagens, principalmente se você estiver interessado em processamento de imagens, automação de tarefas relacionadas a texto e análise de dados. Aqui estão algumas das vantagens de aprender a montar um OCR online com Python:

Aprender a montar um OCR online com Python é uma habilidade valiosa que pode ser aplicada em diversos contextos, desde a digitalização de documentos em escritórios até a automação de tarefas de análise de dados. Além disso, o Python oferece uma ampla gama de recursos e suporte da comunidade, tornando-o uma escolha popular para projetos de OCR.

## Crie o Ambiente Virtual
1. Crie uma pasta no computador;
2. Abra a pasta no VSCode; 
3. Execute o módulo de ambiente virtual (venv): ``` python -m venv venv```
4. Ative o ambiente virtual (windows): ``` ./venv/Script/activate```
5. Mude o interpretador Python do VSCode para o (venv)

## Utilizando uma API de OCR Gratuíta
1. Abra o site: https://ocr.space
2. Registre seu usuário na API: https://ocr.space/ocrapi/freekey
3. Use seu e-mail institucional (unifei.edu.br)
4. Após registro abra seu e-mail
5. Pegue a chave fornecida, exemplo: K12345678901234

## Testando a API
1. Instale a biblioteca requests: ``` (venv): pip install requests```
2. Veja a documentação dos parâmetros da API do OcrSpace em: https://ocr.space/OCRAPI#PostParameters
3. Monte o código abaixo no arquivo ``` ecop06_15_ocr.py``` em uma função:
```python
payload = {'isOverlayRequired': overlay,
           'apikey': api_key,
           'language': language,
           }
with open(filename, 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image',
                      files={filename: f},
                      data=payload,
                      )
return r.content.decode()
```
4. Teste essa função com a imagem: </br><img src="https://www.designerd.com.br/wp-content/uploads/2017/12/regiao-neutra-imagem-alinhar.jpg" width=200/>

## Proposta da Atividade
Usando a função definida anteriormente crie uma aplicação Flask que receba via upload uma imagem em arquivo (jpg ou png) e extraia o texto contido nela. 

1. O texto deverá ser em português, use o google para procurar *imagem com texto*;
2. Faça todo o código embutido no arquivo ``` ecop06_15_ocr.py```, não use páginas templates;
3. A resposta do OCR API deverá voltar na própria página.
4. Salve o arquivo ``` ecop06_15_ocr.py``` no Google Drive após funcionar corretamente.
