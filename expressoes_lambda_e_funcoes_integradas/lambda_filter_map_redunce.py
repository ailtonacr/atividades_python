from functools import reduce


def get_numbers():
    """
    Recebe os números que o usuário deseja elevar ao quadrado, separados por espaço.
    os numeros do tipo float podem ser escritos com vírgula ou ponto
    :return: retorna uma lista com os números que o usuário deseja elevar ao quadrado
    """
    try:
        numbers_to_square = [
            float(number.strip().replace(",", "."))
            for number in input("Digite os números que deseja elevar ao quadrado (separe-os por espaço): ").split()
        ]
        return verify_if_number_is_integer(numbers_to_square)
    except ValueError:
        print("Digite apenas números.")
        get_numbers()


def verify_if_number_is_integer(numbers_to_square):
    """
    :param numbers_to_square: fornece os números para serem verificados
    :return: Verifica se o número é inteiro e o reescreve de forma correta. e 
    retorna uma lista com os números verificados
    """
    return [int(number) if number.is_integer() else number for number in numbers_to_square]


def elevate_to_square(numbers_to_square):
    """
    Executa a função lambda que eleva os números fornecidos ao quadrado para cada número da lista
    :param numbers_to_square: fornece uma lista com os números que o usuário deseja elevar ao quadrado
    :return: retorna uma lista com os números fornecidos elevados ao quadrado
    """
    return list(map(lambda value: value ** 2, numbers_to_square))


def filter_even_numbers(squared_numbers):
    """
    Filtra os números pares da lista de números fornecidos
    :param squared_numbers: fornece uma lista com os números fornecidos elevados ao quadrado
    :return: retorna uma lista com os números pares encontrados em squared_numbers
    """
    return list(filter(lambda value: value % 2 == 0, squared_numbers))


def sum_even_numbers(even_numbers):
    """
    Percorre cada item da lista retornada por filter_even_numbers e soma-os
    utilizando como parâmetro de entrada o resultado da função anterior
    :param even_numbers: fornece uma lista com os números pares encontrados em squared_numbers
    :return: retorna a soma dos números da lista even_numbers
    """
    return reduce(lambda even_num, value: even_num + value, even_numbers)


def view_result(numbers_to_square, squared_numbers, total_even_numbers):
    """
    Imprime:
    - os números fornecidos
    - os números fornecidos elevados ao quadrado
    - a soma dos números pares encontrados em squared_numbers
    :param numbers_to_square: fornece uma lista com os números que o usuário deseja elevar ao quadrado
    :param squared_numbers: fornece uma lista com os números fornecidos elevados ao quadrado
    :param total_even_numbers: fornece a soma dos números pares encontrados em squared_numbers
    """
    print(f"Os números fornecidos foram: {numbers_to_square}")
    print(f"Os numeros fornecidos elevados ao quadrado são: {squared_numbers} ")
    print(f"A soma dos números pares fornecidos elevados ao quadrado é: {total_even_numbers}")


def main():
    numbers_to_square = get_numbers()
    squared_numbers = elevate_to_square(numbers_to_square)
    even_numbers = filter_even_numbers(squared_numbers)
    total_even_numbers = sum_even_numbers(even_numbers)
    view_result(numbers_to_square, squared_numbers, total_even_numbers)


if __name__ == "__main__":
    main()

