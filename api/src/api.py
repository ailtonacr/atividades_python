from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from flask_cors import CORS
from management import add_name, show_guests, remove_name, search_name

app = Flask(__name__)
spec = FlaskPydanticSpec('Ailton', title='API lista de convidados')
spec.register(app)
CORS(app)


@app.route('/add', methods=['POST'])
def add():
    """recebe um nome e o adiciona à lista de convidados"""
    data = request.get_json()
    name = data.get('name')
    result = add_name(name)
    return jsonify(result)


@app.route('/remove', methods=['DELETE'])
def remove():
    """recebe um nome, verifica se está na lista e o remove"""
    data = request.get_json()
    person = data.get('name')
    result = remove_name(person)
    return jsonify(result)


@app.route('/list', methods=['GET'])
def show():
    """mostra a lista de convidados"""
    return jsonify(show_guests())


@app.route('/search', methods=['GET'])
def search():
    """recebe um nome e verifica se está na lista de convidados"""
    data = request.get_json()
    name = data.get('name')
    result = search_name(name)
    return jsonify(result)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)
