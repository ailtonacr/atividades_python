"""
Fiz essa atividade com o intuito de fixar o aprendizado e ver na prática o funcionamento de uma API.
A API fuciona manipulando uma lista de convidados salva em um dicionário.
As ações dela são:
    - Adicionar convidado.
    - Remover convidado.
    - Listar convidados.
    - Buscar convidado na lista.
"""
from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec
from flask_cors import CORS
from src import *

app = Flask(__name__)
spec = FlaskPydanticSpec('Ailton', title='API lista de convidados')
spec.register(app)
CORS(app)


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data.get('name')
    result = add_name(name)
    return result


@app.route('/remove', methods=['DELETE'])
def remove():
    data = request.get_json()
    person = data.get('name')
    result = remove_name(person)
    return result


@app.route('/list', methods=['GET'])
def show():
    return show_guest()


@app.route('/search', methods=['GET'])
def search():
    data = request.get_json()
    name = data.get('name')
    result = search_name(name)
    return result


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)
