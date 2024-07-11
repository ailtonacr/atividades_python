from mymodule import *


def view_result(message):
    print(message)


def trate_dict():
    entered_values = {'value_' + str(i): generate_numbers() for i in range(10)}
    trated_dictionary = process_dict(entered_values)
    view_result(f"Sobre o dicionário que contem os valores: {entered_values.values()}:\n"
                f"A soma total é: {trated_dictionary['sumed_values']},\n"
                f"A média é {trated_dictionary['average_of_values']},\n"
                f"A variação é {trated_dictionary['variation_of_values']}.\n")


def convert_celsius_to_fahrenheit():
    celsius = generate_numbers(0, 100)
    view_result(f"O resultado da conversão de {celsius}ºC para fahrenheit é {c_to_f(celsius)}ºF\n")


def convert_fahrenheit_to_celsius():
    fahrenheit = generate_numbers(0, 212)
    view_result(f"O resultado da conversão de {fahrenheit}ºF para Celsius é {f_to_c(fahrenheit)}ºC\n")


def verify_prime_numbers():
    numbers_for_verify_prime = [generate_numbers(1, 1000) for _ in range(100)]
    view_result(f"Na lista de 100 números aleatórios entre 0 e 1000, foram encontrados os sequintes e números primos:\n"
                f"{primes(numbers_for_verify_prime)}\n")


def items_in_unic_plan():
    items_group = [[generate_numbers() for _ in range(4)] for _ in range(4)]
    view_result(f"Aqui está a lista {items_group} concatenada e organizada em um unico plano:\n"
                f"{sort_items(items_group)}\n")


def phare_in_reverse_plan():
    phrase = 'ailton cruz rodrigues'.split()
    view_result(f"A frase {phrase} com cada palavra escrita inversamente é: {reverse(phrase)}\n")


def tuple_in_random_order():
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

