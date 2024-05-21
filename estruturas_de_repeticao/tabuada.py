"""
Tabuada

- Crie um programa que peça ao usuário para inserir um número.
- Use uma estrutura de repetição para exibir a tabuada desse número de 1 a 10.
- (De extra resolvi adicionar o uso de listas para guardar os resultados)
"""

def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")


def calculate_values(number, tab_values):
    i=1
    while i <=10:
        tab_values.append(number*i)
        i +=1


def view_result(number, tab_values):
    i=0
    while i < 10:
        print(f"{number} x {i+1} = {tab_values[i]}")
        i+=1

def main():
    tab_values = []
    number = get_number("digite o numero que deseja calcular a tabuada de 1 a 10")
    calculate_values(number, tab_values)
    view_result(number, tab_values)


if __name__ == '__main__':
    main()
