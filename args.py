"""
*args
fiz essa atividade apenas pra usar os *args
tava meio sem ideias, coloquei uma busca de numero por indices pra ficar mais interessante
"""


def get_numbers():
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
    return sum(args)


def convert_to_int_or_float(total_sum):
    if total_sum.is_integer():
        return int(total_sum)
    return total_sum


def view_result_and_numbers(result):
    print(f"A soma dos números fornecidos é: {result}")


def search_by_indexes(*args):
    while True:
        index = int(input("Digite o índice do número que deseja ver: "))
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
            return search_by_indexes(*args)
        input("Digite enter para sair, ou qualquer tecla para continuar. ")
        if input() == "":
            break


def main():
    numbers = get_numbers()
    total_sum = calculate_result(*numbers)
    result = convert_to_int_or_float(total_sum)
    view_result_and_numbers(result)
    search_by_indexes(*numbers)


if __name__ == '__main__':
    main()

