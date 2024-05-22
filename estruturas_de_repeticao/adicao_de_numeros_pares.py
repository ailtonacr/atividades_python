"""
Soma de Números Pares

- Crie um programa que some todos os números pares de 1 a 100.
- Use uma estrutura de repetição para iterar através dos números e uma estrutura condicional para verificar se o número é par.
- Exiba a soma total.

# Resolvi deixar a atividade mais interessante, adicionando uma interação com o "somar pares até:".
"""


def get_limit_value(message):
    while True:
        try:
            return int(input(message))
        except:
            print("Digite um valor inteiro")


def get_par_values(par_values, limit_value):
    for i in range(1, limit_value+1):
        if i % 2 == 0:
            par_values.append(i)
        else:
            continue
    return get_limit_value


def sum_values_pairs(par_values):
    return sum(par_values)


def return_result(limit_value, par_values, sum_total_pairs):
    print(f"A soma total de numeros pares presentes de 1 a {limit_value} é {sum_total_pairs}")
    print(f"A quantidade de numeros pares de 1 até {limit_value} é: {len(par_values)}")


def main():
    par_values = []
    limit_value = get_limit_value("Somar pares até:")
    get_par_values(par_values, limit_value)
    sum_total_pairs = sum_values_pairs(par_values)
    return_result(limit_value, par_values, sum_total_pairs)


if __name__ == '__main__':
    main()



