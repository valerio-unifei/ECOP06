# ====== Criando Aplicação Web com o Framework Flask ======

# -- Criar Ambiente Virtual de Desenvolvimento --
# python -m venv ambv
# Linux: source amb/bin/activate
# Windows: ./ambv/Scripts/activate
# (amv): pip install flask flask-sqlalchemy flask-login

# === Aplicação Olá Unifei ===

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
