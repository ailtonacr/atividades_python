guests = {}


def add_name(name):
    """
    Adiciona um nome à lista de convidados.
    :param name: Fornece um nome para adicionar à lista de convidados.
    :return: Retorna uma mensagem de sucesso ou falha.
    """
    if name in guests.values():
        return {"message": f"{name} já está na lista"}
    else:
        guests[f'convidado {len(guests) + 1}'] = name
        return {"message": f"{name} adicionado(a) à lista com sucesso"}


def show_guests():
    """
    Mostra a lista de convidados.
    :return: retorna os convidados. Caso não haja convidados, retorna uma mensagem informando que a lista está vazia.
    """
    if not guests:
        return {"message": "Lista vazia"}
    return guests


def remove_name(name):
    """
    Remove um nome da lista de convidados.
    :param name: fornece um nome para remover da lista de convidados.
    :return: retorna uma mensagem de sucesso ou falha.
    """
    for key, value in guests.items():
        if value == name:
            del guests[key]
            return {"message": f"{name} removido(a) da lista!"}
    return {"message": f"{name} não está na lista!"}


def search_name(name):
    """
    Verifica se um nome está na lista de convidados.
    :param name: fornecido um nome para verificar se está na lista de convidados.
    :return: retorna uma mensagem informando se o nome está ou não na lista.
    """
    for key, value in guests.items():
        if value == name:
            return {"message": f"{name} está na lista"}
    return {"message": f"{name} não está na lista!"}
