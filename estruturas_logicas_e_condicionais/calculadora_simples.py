"""
- Crie um programa que peça ao usuário para inserir dois números e uma operação (adição, subtração, multiplicação, divisão).
- Use estruturas condicionais para executar a operação correta com base na entrada do usuário.
- Exiba o resultado da operação.
"""

from sys import exit


def get_numbers():
    for i in range(3):
        try:
            first_number = float(input('digite o primeiro numero: '))
            second_number = float(input('digite o segundo numero: '))
            return [first_number, second_number]
        except:
            print('digite apenas numeros.')
    exit('Limite de tentativas atingido')


def check_type_numbers(inputted_numbers):
    numbers_checked = inputted_numbers
    for i in range(2):
        if inputted_numbers[i].is_integer():
            numbers_checked[i] = int(inputted_numbers[i])
    return numbers_checked


def get_operator():
    return input('Digite a operação que deseja realizar com os numeros: ').strip().lower()


def make_operation(operator, numbers_for_operation, cont):  # TODO: mudar o match para dictionary
    while cont < 3:
        match operator:
            case "vezes" | "multiplicar" | "multiplicação" | "x" | "*" | "multiplique":
                return "x", numbers_for_operation[0] * numbers_for_operation[1]
            case "mais" | "adição" | "adicionar" | "somar" | "some" | "+" | "adicione":
                return "+", numbers_for_operation[0] + numbers_for_operation[1]
            case "dividir" | "divisão" | "divide" | "divida" | "/":
                return "/", numbers_for_operation[0] / numbers_for_operation[1]
            case "subtrair" | "subtração" | "menos" | "-" | "subtraia" | "subtrai":
                return "-", numbers_for_operation[0] - numbers_for_operation[1]
            case _:
                print('Digite uma operação válida.')
                operator = get_operator()
                return make_operation(operator, numbers_for_operation, cont + 1)
    exit('Limite de tentativas atingido')


def check_type_result(result_of_operation):
    if result_of_operation.is_integer():
        return int(result_of_operation)
    else:
        return result_of_operation


def view_result(operator, numbers_for_operation, final_result):
    print(f'O resultado de {numbers_for_operation[0]} {operator} {numbers_for_operation[1]} é {final_result}')


def main():
    inputted_numbers = get_numbers()
    numbers_for_operation = check_type_numbers(inputted_numbers)
    operator = get_operator()
    operator, result_of_operation = make_operation(operator, numbers_for_operation, 0)
    final_result = check_type_result(result_of_operation)
    view_result(operator, numbers_for_operation, final_result)


if __name__ == '__main__':
    main()