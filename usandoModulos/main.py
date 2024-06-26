from mymodule import *


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
    items_group = [[gen() for _ in range(4)] for _ in range(4)]
    celsius = gen(0, 100)
    fahrenheit = gen(0, 212)
    entered_values = {'value_' + str(i): gen() for i in range(10)}
    phrase = 'ailton cruz rodrigues'.split()
    tuple_listing = [tuple(gen() for _ in range(gen(1, 10))) for _ in range(4)]
    numbers_for_veryfy_prime = [gen(1, 1000) for _ in range(100)]

    trated_dictionary = process_dict(entered_values)
    C_to_F = ctof(celsius)
    F_to_C = ftoc(fahrenheit)
    pryme_numbers = primes(numbers_for_veryfy_prime)
    result_items_in_unic_plan = ordene(items_group)
    reverse_phrase = order(phrase)
    list_tuple_in_random_order = random_order(tuple_listing)

    view_results(celsius, fahrenheit, C_to_F, F_to_C, pryme_numbers, items_group, result_items_in_unic_plan, entered_values,
                 trated_dictionary, phrase, reverse_phrase, tuple_listing, list_tuple_in_random_order)


if __name__ == '__main__':
    main()

