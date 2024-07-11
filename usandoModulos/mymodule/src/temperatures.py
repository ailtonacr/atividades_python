def c_to_f(celsius):
    """
    Faz a conversão de celsius para fahrenheit
    :param celsius: Fornece a temperatura em celsius a ser convertida em fahrenheit
    :return: retorna a temperatura em fahrenheit, com apenas uma casa decimal depois da ",".
    """
    fahrenheit = (9 / 5) * celsius + 32
    return round(fahrenheit, 1)


def f_to_c(fahrenheit):
    """
    Faz a conversão de fahrenheit para celsius
    :param fahrenheit: Fornece a temperatura em fahrenheit a ser convertida em celsius
    :return: retorna a temperatura em celsius, com apenas uma casa decimal depois da ",".
    """
    celsius = fahrenheit / (9 / 5) - 32
    return round(celsius, 1)

