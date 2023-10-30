# Aplicação Web pelo Framework Flask

O Flask é um framework web em Python que é amplamente utilizado para o desenvolvimento de aplicativos web e APIs de forma rápida e simples. Criado por Armin Ronacher, o Flask é conhecido por sua simplicidade e facilidade de uso, sendo uma escolha popular entre desenvolvedores para projetos de todos os tamanhos.

Pontos-chave sobre o Flask:
1. Micro Framework: O Flask é muitas vezes referido como um "micro framework" porque oferece apenas o conjunto mínimo de ferramentas necessárias para criar aplicativos web, deixando grande parte da arquitetura e decisões de design para os desenvolvedores. Isso dá aos desenvolvedores a liberdade de escolher as bibliotecas e ferramentas que desejam usar em seus projetos.
2. Simplicidade: Uma das principais características do Flask é sua simplicidade. Ele possui uma API limpa e fácil de entender, o que o torna uma excelente escolha para iniciantes e para desenvolvedores que desejam criar aplicativos rapidamente.
3. Extensibilidade: Embora seja um micro framework, o Flask é altamente extensível. Você pode adicionar funcionalidades extras ao seu aplicativo usando extensões que fornecem recursos como autenticação, manipulação de formulários, integração de bancos de dados, e muito mais.
4. Werkzeug e Jinja2: Flask se baseia no Werkzeug, que é uma biblioteca WSGI (Web Server Gateway Interface) para manipulação de solicitações HTTP, e no Jinja2, um mecanismo de template que facilita a criação de páginas da web dinâmicas.
5. Roteamento flexível: Flask oferece um sistema de roteamento flexível que permite mapear URLs para funções Python, tornando fácil a criação de endpoints para diferentes partes do seu aplicativo.
6. Desenvolvimento e depuração simplificados: O Flask possui uma ferramenta de depuração embutida que ajuda a identificar e corrigir erros durante o desenvolvimento. Além disso, é adequado para ambientes de desenvolvimento e produção.
7. Comunidade ativa: Flask tem uma comunidade ativa e uma ampla gama de recursos, incluindo tutoriais, documentação e extensões de terceiros, o que facilita o desenvolvimento de aplicativos robustos.

## Ambiente Virtual

Toda aplicação web precisa de um ambiente isolado para desenvolvimento que não interfira as outras instalações ou programas Python desenvolvidos na máquina de execução, por isso a necessidade da criação de um ambiente virtual.

Segue os passos para essa criação:
1. Crie uma pasta em um local do computador com permissão de escrita ou leitura (pode ser um pendrive);
2. Abra o VSCode e solicite abrir essa pasta;
3. Abra o terminal do VSCode;
4. Execute o comando: ``` python -m venv venv ```
5. Aguarde a criação da pasta "venv" no projeto;
6. Execute o ambiente virtual ``` ./venv/Scripts/activate ```
7. Mude o interpretador Python para o ambiente virtual no VSCode
8. Deverá aparecer **Python 3.10.12 (venv)**

## Instalando bibliotecas no Ambiente Virtual
```
(venv): pip install flask flask-sqlalchemy flask-login
```

## Aplicação Teste

Crie um arquivo app1.py com o seguinte código:

```
from flask import Flask
# cria a aplicação Flask
app = Flask(__name__)

# endereço raiz do site
@app.route('/')
def index():
    return "<h1>Olá UNIFEI!</h1>"

# endereço do usuário do site
@app.route('/usuario/<nome>')
def usuario(nome):
	return '<h1>Olá, {0}!</h1>'.format(nome)

# executando o servido de página 
app.run(debug=True)
```

Execute o arquivo.

Conceitos apresentados:
1. O que são rotas de URL?
2. O uso de "decorators" nas funções
3. Parâmetros de rotas
4. HTML

## Modelos HTML

Crie uma pasta "templates" no projeto e coloque o seguintes arquivos:

*index.html*
```
<h1>Hello World!</h1>
```

*usuario.html*
```
<h1>Hello, {{nome}}!</h1>
```

Crie um arquivo "app2.py" com:
```
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/usuario/<nome>')
def usuario(nome):
  return render_template('usuario.html', nome=nome)

app.run(debug=True)
```

Execute.

## Formulário de Dados de Entrada

Modifique o arquivo *index.html* na pasta "templates":

```html
<!DOCTYPE HTML>
<html>
  <head>
    <title>UNIFEI-Flask</title>
  </head>
  <body>
    <form method="POST" action="">
      Qual é seu nome? <input type="text" name="nome">
      <input type="submit" name="submit" value="Enviar">
    </form>
    {% if nome %}
      <h1>Olá, {{nome}}!</h1>
    {% endif %}
  </body>
</html>
```

Crie o "app3.py" com :
```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nome = None
    if request.method == 'POST' and 'nome' in request.form:
      nome = request.form['nome']
    return render_template('index.html', nome=nome)

if __name__ == 'main':
   app.run(debug=True)
```

Execute.

Conceitos apresentados aqui:
1. Formulário e campos de entrada
2. Rotas com comandos GET e POST
3. Estruturas embutidas Python (Jinja2) no HTML

# Gerar um site em produção
Crie um repositório com o último projeto.
Use o site [Render](render.com) para subir seu site on-line.


