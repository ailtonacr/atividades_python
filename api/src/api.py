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
    """Recebe um nome e o adiciona à lista de convidados"""
    data = request.get_json()
    name = data.get('name')
    try:
        add_name(name)
    except Exception as e:
        return jsonify({"message": str(e)})

    return jsonify({"message": f'{name} adicionado(a) à lista com sucesso'})


@app.route('/remove', methods=['DELETE'])
def remove():
    """Recebe um nome, verifica se está na lista e o remove"""
    data = request.get_json()
    name = data.get('name')
    try:
        remove_name(name)
    except Exception as e:
        return jsonify({"message": str(e)})

    return jsonify({"message": f'{name} removido(a) da lista!'})


@app.route('/list', methods=['GET'])
def show():
    """Mostra a lista de convidados"""
    guests = show_guests()
    if guests is None:
        return jsonify({"message": "Lista vazia"})
    return jsonify(guests)


@app.route('/search', methods=['GET'])
def search():
    """Recebe um nome e verifica se ele está na lista de convidados"""
    data = request.get_json()
    name = data.get('name')
    if search_name(name):
        return jsonify({"message": f'{name} está na lista'})
    return jsonify({"message": f'{name} não está na lista!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)
