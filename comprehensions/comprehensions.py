"""
crie uma função que receba vários números em uma única string separados por espaço e imprime a soma desses números.
OBS: Utilize list comprehension para facilitar a manipulação da string de entrada.
"""


def get_numbers():
    """
    Recebe os números que o usuário deseja somar, separados por espaço
    os numeros do tipo float podem ser escritos com vírgula ou ponto
    :return: retorna uma lista com os números que o usuário deseja somar
    """
    try:
        numbers_for_sum = [float(number.strip().replace(",", ".")) for number in input("Digite os números que deseja somar (separe-os por espaço): ").split()]
        return [int(number) if number.is_integer() else number for number in numbers_for_sum]
    except ValueError:
        print("Digite apenas números.")
        get_numbers()


def view_result_and_numbers(total_sum, numbers_for_sum):
    """
    Exibe o resultado da soma dos números fornecidos e os números fornecidos
    :param total_sum: fornece o resultado da soma dos números fornecidos
    :param numbers_for_sum: fornece a lista com os números fornecidos pelo usuário
    """
    print(f"A soma dos números fornecidos é: {total_sum}")
    print(f"Os números fornecidos foram: {numbers_for_sum}")


def main():
    """
    declara as variáveis principais
    chama as funções necessárias para a execução do programa em suas respectivas ordens
    """
    numbers_for_sum = get_numbers()
    total_sum = sum(numbers_for_sum)
    view_result_and_numbers(total_sum, numbers_for_sum)


if __name__ == "__main__":
    main()

