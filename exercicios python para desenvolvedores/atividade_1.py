"""
Meus objetivos com esses exercícios foram:

1 - Implementar duas funções:

    Uma que converta temperatura em graus Celsius para Fahrenheit.
    Outra que converta temperatura em graus Fahrenheit para Celsius.

2 - Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.

    Neste caso aqui, ficou muito abstrato (quem é True e quem é False?) então resolvi agrupar os mesmos em uma lista.

3 - Implementar uma função que receba uma lista de listas de comprimentos quaisquer e retorne uma lista de uma dimensão.

4 - Implementar uma função que receba um dicionário e retorne a soma, a média e a variação dos valores.

5 - Escreva uma função que:

    Receba uma frase como parâmetro.
    Retorne uma nova frase com cada palavra com as letras invertidas.

6 - Crie uma função que:

    Receba uma lista de tuplas (dados), um inteiro e um booleano.
    Retorne dados ordenados pelo item indicado pela chave e em ordem decrescente se reverso for verdadeiro.


Para criar uma aleatóriedade e simular variações de dados, fiz algumas modificaçõs, foram elas:

Removi interações com o usuário e variaveis com valores pré definidos, pra isso usei a função randint, do pacote random.

no item 3, ao invés de predefinir o tamanho das tuplas, coloquei pra selecionar um valor aleatório entre 1 e 10,
assim se encaixa melhor no que pede o enunciado.

Também tentei aplicar o conceito de reutilização de funções, pra manter um código menos repetitivo.
"""


from functools import reduce
from random import randint


def convert_celsius_to_fahrenheit(celsius):
    """
    Faz a conversão de celsius para fahrenheit
    :param celsius: Fornece a temperatura em celsius a ser convertida em fahrenheit
    :return: retorna a temperatura em fahrenheit, com apenas uma casa decimal depois da ",".
    """
    fahrenheit = (9 / 5) * celsius + 32
    return round(fahrenheit, 1)


def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Faz a conversão de fahrenheit para celsius
    :param fahrenheit: Fornece a temperatura em fahrenheit a ser convertida em celsius
    :return: retorna a temperatura em celsius, com apenas uma casa decimal depois da ",".
    """
    celsius = fahrenheit / (9 / 5) - 32
    return round(celsius, 1)


def verify_prime_numbers(numbers_for_veryfy_prime):
    """
    Percorre a lista "numbers_for_veryfy_prime" e verifica se o número encontrado é ou não um número primo.
    Se for, o número é adicionado à lista "prime_numbers"
    :param numbers_for_veryfy_prime: Fornece uma lista com 100 números aleatórios de 1 a 1000
    :return: Retorna uma lista com os números primos encontardos na lista "numbers_for_verify_prime".
    """
    prime_numbers = []
    for value in numbers_for_veryfy_prime:
        mult = 0
        for count in range(2, value):
            if value % count == 0:
                mult += 1

        if mult == 0 and value != 1:
            prime_numbers.append(value)

    return prime_numbers


def get_ramdom_numbers(initial_value=0, final_value=100):
    """
    Gera números aleatórios de acordo com os parametros fornecidos.
    Por padrão são: initial_value=0 e final_value=100
    :param initial_value: Fornece o valor inicial para geração de números aleatórios
    :param final_value: Fornece o valor final para geração de números aleatórios
    :return: Retornq um número inteiro aleatório contido no intervalo entre initial_value e final_value.
    """
    return randint(initial_value, final_value)


def items_concatenation(previous_result, next_item):
    """
    :return: Rotorna a concatenação dos dois parâmetros fornecidos (previous_result e next_item)
    """
    return previous_result + next_item


def items_ordenation(item, in_order=True):
    """
    Recebe um item a ser ordenado, De acordo com o parâmetro "in_order"
    Se o parâmetro "in_order" for false, retorna o item na ordem reversa.
    :param item: Fornece o item que deseja ordenar
    :param in_order: Fornece pra função a ordem desejada do item.
    """
    if in_order is False:
        return item[::-1]
    return item


def items_in_unic_plan(items_group):
    """
    Agrupa toodos items de "items_group" em uma única lista e or retorma de forma ordenada.
    :param items_group: Fornece um grupo de itens (tuplas ou listas)
    """
    return sorted(reduce(items_concatenation, items_group))


def dictionary_processing(entered_values):
    """
    Processa o dicionário fornecido por "entered_values" da seguinte forma:
    Soma todos os valores do dicionário e armazena em "sumed_values"
    Verifica a média entre o maior valor e o menor valor e armazena em "average_of_values"
    Verifica a variação entre o maior valor e o menor valor e armazena em "variation_of_values"
    :param entered_values: fornece um dicionário com 10 valores inteiros aleatórios entre 0 e 100
    :return:Retorna um dicionário com o resultado do processamento de "entered_values"
    """
    sumed_values = sum(entered_values.values())
    average_of_values = round(sumed_values / len(entered_values), 2)
    variation_of_values = max(entered_values.values()) - min(entered_values.values())
    return {'sumed_values': sumed_values, 'average_of_values': average_of_values,
            'variation_of_values': variation_of_values}


def reverse_caracters_of_phrase(phrase):
    """
    Percorre a lista fornecida pelo parâmetro "phrase"
    Para cada item nela, executa a função que adiciona o item escrito de forma inversa
    na lista "phrase_with_reversed_caracteres".
    :param phrase: Fornece uma lista com uma frase separada em strings
    :return: Retorna a frase com cada palavra escrita de forma inversa
    """
    phrase_with_reversed_caracters = []
    for i in range(len(phrase)):
        phrase_with_reversed_caracters.append(items_ordenation(phrase[i], False))
    return phrase_with_reversed_caracters


def random_order_list(tuple_listing):
    """
    Recebe a lista de tuplas fornecida por "tuple_list", concatena todos os itens contidos nela
    e os armazena de forma ordenada em "tuple_listing_ordened".
    a variável "in_order" armazena um valor booleano aleatório que determina se
    a lista "tuple_listing_ordened" vai ser retornada em ordem crescente ou decrescente.
    :param tuple_listing: fornece uma lista de 4 tuplas contendo uma quantidade aleatória (limitado a 10 números)
     de números aleatórios de 0 a 100 em cada uma delas.
    :return: Retorna uma lista com os items de "tuple_list_ordened" na ordem fornecida por "in_order"
    """
    tuple_listing_ordened = sorted(reduce(items_concatenation, tuple_listing))
    in_order = bool(get_ramdom_numbers(final_value=1))
    return items_ordenation(tuple_listing_ordened, in_order=in_order)


def view_results(celsius, fahrenheit, C_to_F, F_to_C, pryme_numbers, items_group, result_items_in_unic_plan, entered_values,
                 trated_dictionary, phrase, reverse_phrase, tuple_listing, list_tuple_in_random_order):
    print(f"O resultado da conversão de {fahrenheit}ºF para Celsius é {F_to_C}ºC\n")
    print(f"O resultado da conversão de {celsius}ºC para fahrenheit é {C_to_F}ºF\n")
    print(f"Na lista de 100 números aleatórios entre 0 e 1000, foram encontrados os sequintes e números primos:\n"
          f"{pryme_numbers}\n\n")
    print(f"Aqui está a lista {items_group} concatenada e organizada em um unico plano:\n"
          f"{result_items_in_unic_plan}\n\n")
    print(f"Sobre o dicionário que contem os valores: {entered_values}:\n"
          f"A soma total é: {trated_dictionary['sumed_values']},\n"
          f"A média é {trated_dictionary['average_of_values']},\n"
          f"A variação é {trated_dictionary['variation_of_values']}.\n\n")
    print(f"A frase {phrase} com cada palavra escrita inversamente é: {reverse_phrase}\n")
    print(f"A lista de tuplas fornecisda foi: {tuple_listing}.\n")
    print(f"Aqui esta uma lista com os valores devidamente concatenados e ordenados:\n"
          f"{list_tuple_in_random_order}")


def main():
    items_group = [[get_ramdom_numbers() for _ in range(4)] for _ in range(4)]
    celsius = get_ramdom_numbers(final_value=40)
    fahrenheit = get_ramdom_numbers(final_value=212)
    entered_values = {'value_' + str(i): get_ramdom_numbers() for i in range(10)}
    phrase = 'ailton cruz rodrigues'.split()
    tuple_listing = [tuple(get_ramdom_numbers() for _ in range(get_ramdom_numbers(initial_value=1, final_value=10))) for _ in range(4)]
    numbers_for_veryfy_prime = [get_ramdom_numbers(1, 1000) for _ in range(100)]

    trated_dictionary = dictionary_processing(entered_values)
    C_to_F = convert_celsius_to_fahrenheit(celsius)
    F_to_C = convert_fahrenheit_to_celsius(fahrenheit)
    pryme_numbers = verify_prime_numbers(numbers_for_veryfy_prime)
    result_items_in_unic_plan = items_in_unic_plan(items_group)
    reverse_phrase = reverse_caracters_of_phrase(phrase)
    list_tuple_in_random_order = random_order_list(tuple_listing)

    view_results(celsius, fahrenheit, C_to_F, F_to_C, pryme_numbers, items_group, result_items_in_unic_plan, entered_values,
                 trated_dictionary, phrase, reverse_phrase, tuple_listing, list_tuple_in_random_order)


if __name__ == "__main__":
    main()

