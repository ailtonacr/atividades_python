"""
*args
fiz essa atividade apenas pra usar os *args
tava meio sem ideias, coloquei uma busca de numero por indices pra ficar mais interessante
"""
from sys import exit


def get_numbers():
    """
    Recebe os números que o usuário deseja somar, separados por espaço
    :return: retorna uma lista com os números que o usuário deseja somar
    """
    numbers_for_sum = []
    print("Digite um número por vez. Tecle enter para sair e ver o resultado da soma dos números fornecidos.")
    while True:
        try:
            number = input("Digite um número: ")
            if number == "":
                break
            numbers_for_sum.append(float(number))
        except ValueError:
            print("Digite um número válido.")
    return numbers_for_sum


def calculate_result(*args):
    """
    Calcula a soma dos números fornecidos
    :param args: fornece os numeros inseridos pelo usuário como argumentos posicionais
    :return: retorna a soma dos números fornecidos
    """
    return sum(args)


def convert_to_int_or_float(total_sum):
    """
    Converte o resultado da soma dos números fornecidos para inteiros ou floats
    :param total_sum: fornece o resultado da soma dos números fornecidos
    :return: retorna o resultado da soma dos números fornecidos como inteiros ou floats
    """
    if total_sum.is_integer():
        return int(total_sum)
    return total_sum


def view_result_and_numbers(result):
    """
    Exibe o resultado da soma dos números fornecidos
    :param result: fornece o resultado da soma dos números fornecidos
    """
    print(f"A soma dos números fornecidos é: {result}")


def search_by_indexes(*args):
    """
    Busca um número na lista de números fornecidos pelo usuário através de um índice
    :param args: fornece os números inseridos pelo usuário como argumentos posicionais
    :return: em caso de erro, retorna para a função search_by_indexes
    ao final da execução, pergunta ao usuário se ele deseja consultar outro indice ou encerrar do programa
    """
    while True:
        index = int(input("Digite o índice do número que deseja consultar: "))
        try:
            if index < 0:
                raise ValueError
            elif index >= len(args):
                raise ValueError
            elif args[index].is_integer():
                number = int(args[index])
            elif args[index].is_integer() is False:
                number = args[index]
            print(f"{number} é o número no índice {index}.")
        except ValueError:
            print("Digite um índice válido.")
            search_by_indexes(*args)
        if input("Digite enter para encerrar o programa, ou qualquer tecla para consultar outro indice. ") == "":
            exit("Programa encerrado.")


def main():
    """
    declara as variáveis principais
    chama as funções necessárias para a execução do programa em suas respectivas ordens
    """
    numbers = get_numbers()
    total_sum = calculate_result(*numbers)
    result = convert_to_int_or_float(total_sum)
    view_result_and_numbers(result)
    search_by_indexes(*numbers)


if __name__ == '__main__':
    main()

