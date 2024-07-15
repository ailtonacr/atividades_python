from flask import jsonify

guest = {}


def add_name(name):
    if name in guest.values():
        return jsonify({"message": f"{name} já está na lista"})
    else:
        guest[f'convidado {len(guest) + 1}'] = name
        return jsonify({"message": f"{name} adicionado(a) à lista com sucesso"})


def show_guest():
    if not guest:
        return jsonify({"message": "Lista vazia"})
    return jsonify(guest)


def remove_name(name):
    for key, value in guest.items():
        if value == name:
            del guest[key]
            return jsonify({"message": f"{name} removido(a) da lista!"})
    return jsonify({"message": f"{name} não está na lista!"})


def search_name(name):
    for key, value in guest.items():
        if value == name:
            return jsonify({"message": f"{name} está na lista"})
    return jsonify({"message": f"{name} não está na lista!"})