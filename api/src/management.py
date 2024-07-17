guests = {}


def add_name(name):
    """
    Adiciona um nome à lista de convidados.
    :param name: Fornece um nome em formato de string para adicionar à lista de convidados.
    """
    if name in guests.values():
        return False
    guests[f'convidado {len(guests) + 1}'] = name
    return True


def show_guests():
    """
    Mostra a lista de convidados.
    :return: Retorna os convidados. Caso não haja convidados, retorna None.
    """
    if not guests:
        return None
    return guests


def remove_name(name):
    """
    Remove um nome da lista de convidados.
    :param name: Fornece um nome para remover da lista de convidados.
    :return: Retorna True se o nome foi removido, False caso contrário.
    """
    for key, value in guests.items():
        if value == name:
            del guests[key]
            return True
    return False


def search_name(name):
    """
    Verifica se um nome está na lista de convidados.
    :param name: Fornece um nome para verificar se está na lista de convidados.
    :return: Retorna True se o nome está na lista, False caso contrário.
    """
    return name in guests.values()
