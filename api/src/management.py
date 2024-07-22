guests = {}


def add_name(name):
    """
    Adiciona um nome à lista de convidados.
    :param name: Fornece um nome em formato de string para adicionar à lista de convidados.
    """
    if name in guests.values():
        raise Exception(f'"{name}" já está na lista')
    guests[f'convidado {len(guests) + 1}'] = name


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
    """
    if name not in guests.values():
        raise Exception(f'"{name}" não está na lista!')
    for key, value in guests.items():
        if value == name:
            del guests[key]
            break


def search_name(name):
    """
    Verifica se um nome está na lista de convidados.
    :param name: Fornece um nome para verificar se está na lista de convidados.
    :return: Retorna True se o nome está na lista, False caso contrário.
    """
    return name in guests.values()
