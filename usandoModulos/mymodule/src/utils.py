from random import randint
from functools import reduce


def random_order(item_listing):
    """
    Recebe a lista de tuplas fornecida por "tuple_list", concatena todos os itens contidos nela
    e os armazena de forma ordenada em "tuple_listing_ordened".
    a variável "in_order" armazena um valor booleano aleatório que determina se
    a lista "tuple_listing_ordened" vai ser retornada em ordem crescente ou decrescente.
    :param tuple_listing: fornece uma lista de 4 tuplas contendo uma quantidade aleatória (limitado a 10 números)
     de números aleatórios de 0 a 100 em cada uma delas.
    :return: Retorna uma lista com os items de "tuple_list_ordened" na ordem fornecida por "in_order"
    """
    tuple_listing_ordened = sorted(reduce(concat, item_listing))
    return order(tuple_listing_ordened, in_order=tf())


def concat(previous_result, next_item):
    """
    :return: Rotorna a concatenação dos dois parâmetros fornecidos (previous_result e next_item)
    """
    return previous_result + next_item


def gen(initial=0, final=100):
    """
    Gera números aleatórios de acordo com os parametros fornecidos.
    Por padrão são: initial_value=0 e final_value=100
    :param initial: Fornece o valor inicial para geração de números aleatórios
    :param final: Fornece o valor final para geração de números aleatórios
    :return: Retornq um número inteiro aleatório contido no intervalo entre initial_value e final_value.
    """
    return randint(initial, final)


def order(item, in_order=True):
    """
    Recebe um item a ser ordenado, De acordo com o parâmetro "in_order"
    Se o parâmetro "in_order" for false, retorna o item na ordem reversa.
    :param item: Fornece o item que deseja ordenar
    :param in_order: Fornece pra função a ordem desejada do item.
    """
    if in_order is False:
        return item[::-1]
    return item


def ordene(itens_group):
    """
    Agrupa toodos items de "items_group" em uma única lista e or retorma de forma ordenada.
    :param itens_group: Fornece um grupo de itens (tuplas ou listas)
    """
    return sorted(reduce(concat, itens_group))


def tf():
    """
    :return: retorna um valor booleano aleatório
    """
    return bool(gen(0, 1))


def reverse(item):
    """
    Percorre a lista fornecida pelo parâmetro "phrase"
    Para cada item nela, executa a função que adiciona o item escrito de forma inversa
    na lista "phrase_with_reversed_caracteres".
    :param item: Fornece uma lista com uma frase separada em strings
    :return: Retorna a frase com cada palavra escrita de forma inversa
    """
    item_reversed = []
    for i in range(len(item)):
        item_reversed.append(order(item[i], False))
    return item_reversed


def process_dict(item):
    """
    Processa o dicionário fornecido por "entered_values" da seguinte forma:
    Soma todos os valores do dicionário e armazena em "sumed_values"
    Verifica a média entre o maior valor e o menor valor e armazena em "average_of_values"
    Verifica a variação entre o maior valor e o menor valor e armazena em "variation_of_values"
    :param item: fornece um dicionário com 10 valores inteiros aleatórios entre 0 e 100
    :return:Retorna um dicionário com o resultado do processamento de "entered_values"
    """
    sumed_values = sum(item.values())
    average_of_values = round(sumed_values / len(item), 2)
    variation_of_values = max(item.values()) - min(item.values())
    return {'sumed_values': sumed_values, 'average_of_values': average_of_values,
            'variation_of_values': variation_of_values}


def primes(numbers):
    """
    Percorre a lista "numbers" e verifica se o número encontrado é ou não um número primo.
    Se for, o número é adicionado à lista "prime_numbers"
    :param numbers: Fornece uma lista com 100 números aleatórios de 1 a 1000
    :return: Retorna uma lista com os números primos encontardos na lista "numbers".
    """
    prime_numbers = []
    for value in numbers:
        mult = 0
        for count in range(2, value):
            if value % count == 0:
                mult += 1

        if mult == 0 and value != 1:
            prime_numbers.append(value)

    return prime_numbers
