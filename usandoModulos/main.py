from mymodule import *


def view_result(message):
    print(message)


def trate_dict():
    """
    Gera o dicionário entered_values com 10 valores aleatórios e passa esse dicionário para a função process_dict,
    que retorna a soma total, a média e a variação dos valores.
    Esses valores são exibidos na tela usando a função view_result.
    """
    entered_values = {'value_' + str(i): generate_numbers() for i in range(10)}
    trated_dictionary = process_dict(entered_values)
    view_result(f"""Sobre o dicionário que contém os valores: {entered_values.values()}:
A soma total é: {trated_dictionary['sumed_values']}
A média é: {trated_dictionary['average_of_values']}
A variação é: {trated_dictionary['variation_of_values']}.\n""")


def convert_celsius_to_fahrenheit():
    """
    Gera um valor aleatório entre 0 e 100 e passa esse valor para a função c_to_f, que retorna o valor convertido
    para fahrenheit.
    O resultado é exibido na tela usando a função view_result.
    """
    celsius = generate_numbers(0, 100)
    view_result(f"O resultado da conversão de {celsius}ºC para fahrenheit é {c_to_f(celsius)}ºF\n")


def convert_fahrenheit_to_celsius():
    """
    Gera um valor aleatório entre 0 e 212 e passa esse valor para a função f_to_c, que retorna o valor convertido
    para celsius.
    O resultado é exibido na tela usando a função view_result.
    """
    fahrenheit = generate_numbers(0, 212)
    view_result(f"O resultado da conversão de {fahrenheit}ºF para Celsius é {f_to_c(fahrenheit)}ºC\n")


def verify_prime_numbers():
    """
    Gera uma lista de 100 números aleatórios entre 0 e 1000 e passa essa lista para a função primes, que retorna
    os números primos encontrados.
    O resultado é exibido na tela usando a função view_result.
    """
    numbers_for_verify_prime = [generate_numbers(1, 1000) for _ in range(100)]
    view_result(f"Na lista de 100 números aleatórios entre 0 e 1000, foram encontrados os sequintes e números primos:\n"
                f"{primes(numbers_for_verify_prime)}\n")


def items_in_unic_plan():
    """
    Gera uma lista de 4 listas com 4 valores aleatórios e passa essa lista para a função sort_items, que retorna
    os valores concatenados e ordenados em ordem crescente.
    O resultado é exibido na tela usando a função view_result.
    """
    items_group = [[generate_numbers() for _ in range(4)] for _ in range(4)]
    view_result(f"Aqui está a lista {items_group} concatenada e organizada em um unico plano:\n"
                f"{sort_items(items_group)}\n")


def phare_in_reverse_plan():
    """
    Gera uma lista com uma frase e passa essa lista para a função reverse, que retorna a frase com cada palavra
    escrita de forma inversa.
    O resultado é exibido na tela usando a função view_result.
    """
    phrase = 'ailton cruz rodrigues'.split()
    view_result(f"A frase {phrase} com cada palavra escrita inversamente é: {reverse(phrase)}\n")


def tuple_in_random_order():
    """
    Gera uma lista de 4 tuplas com até 4 valores aleatórios. Passa essa lista para a função random_order,que concatena
    os valores das tuplas e os retorna em uma lista ordenada de forma aleatória (cresecente ou decrescente)
    O resultado é exibido na tela usando a função view_result.
    """
    tuple_listing = [tuple(generate_numbers() for _ in range(generate_numbers(1, 10))) for _ in range(4)]
    view_result(f"A lista de tuplas fornecisda foi: {tuple_listing}.\n"
                f"Aqui esta uma lista com os valores devidamente concatenados e ordenados:\n"
                f"{random_order(tuple_listing)}")


def main():
    trate_dict()
    convert_celsius_to_fahrenheit()
    convert_fahrenheit_to_celsius()
    verify_prime_numbers()
    items_in_unic_plan()
    phare_in_reverse_plan()
    tuple_in_random_order()


if __name__ == '__main__':
    main()

