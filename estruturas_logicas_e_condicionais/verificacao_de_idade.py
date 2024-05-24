"""
Verificação de Idade

- Crie um programa que peça ao usuário para inserir seu ano de nascimento.
- Use uma estrutura condicional para verificar a faixa etária do usuário.
- Exiba uma mensagem apropriada com base na faixa etária.
- Pra calcular a idade resolvi fazer um import do ano atual, pra isso tive que pedir ajuda ao gepeto, pois não tive
contato com o assunto ainda, pedi ajuda na formatação datetime.now().year pra pegar apenas o ano (Obrigado Thalita,
essa ideia veio por causa daquele today kkk)
"""
from datetime import datetime
import sys


def get_year_of_birth(message):
    for i in range(3):
        try:
            year = int(input(message))
            if len(str(year)) != 4:
                print('O ano de nascimento deve ter 4 digitos.')
                continue
            return year
        except:
            print('Data de nascimento inválida.')
    sys.exit('Limite de tentaivas excedido')


def calculate_age(year_of_birth):
    current_year = datetime.now().year
    return current_year - year_of_birth


def check_age_range(age):
    if age >= 65:
        return 'idoso'
    elif age >= 18:
        return 'adulto'
    elif age >= 13:
        return 'adolescente'
    else:
        return 'infantil'


def view_age_and_age_range(age, age_range):
    print(f'você tem {age} anos e está na faixa etária "{age_range}"')


def main():
    year_of_birth = get_year_of_birth('Digite o ano em que você nasceu:')
    age = calculate_age(year_of_birth)
    age_range = check_age_range(age)
    view_age_and_age_range(age, age_range)


if __name__ == '__main__':
    main()

