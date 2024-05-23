"""
Tabuada

- O usuário deve informar um número para calcular a tabuada do mesmo.
- Uma strutura de repetição deve ser usada para calcular a tabuada desse número de 1 a 10.
- Use uma estrutura de repetição deve exibir a tabuada desse número de 1 a 10.
- Usei listas para armazenar os valores da tabuada.
"""


def get_number(message):
    try:
        return int(input(message))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        return get_number(message)


def calculate_values(number, tab_values):
    values = tab_values
    i = 1
    for i in range(1, 11):
        values.append(number*i)
        i += 1
    return values


def view_result(number, tab_values):
    i = 0
    for i in range(10):
        len(tab_values)
        print(f"{number} x {i + 1} = {tab_values[i]}")
        i += 1


def main():
    tab_values = []
    number = get_number("digite o numero que deseja calcular a tabuada de 1 a 10")
    tab_values = calculate_values(number, tab_values)
    view_result(number, tab_values)


if __name__ == '__main__':
    main()

