"""
Atividade: Gerenciador de Listas de Compras
Você vai criar um sistema simples de gerenciamento de listas de compras.
O sistema permitirá adicionar itens à lista, remover itens da lista,
editar a quantidade de itens e mostrar os itens da lista.
objetivos:
uso de dicionários
uso de parâmetros padrão
uso de **kwargs
uso de *args #esse aqui eu vou fazer em uma separada, não encontrei um uso interessante pra ele aqui.
"""


from sys import exit

shopping_cart = {}


def select_actions():
    """
    Solicita ao usuário que selecione uma ação a ser executada.
    O usuário tem até três tentativas para inserir um valor válido.
    Se todas as tentativas forem inválidas, o programa será encerrado.
    """
    for i in range(3):
        try:
            action = input("\nSelecione uma opção:\n"
                           "1. adicionar items a lista\n"
                           "2. remover items da lista\n"
                           "3. editar quantidade de itens\n"
                           "4. mostrar itens da lista\n"
                           "5. sair\n"
                           )
            if int(action) not in range(1, 6):
                raise ValueError
            return action
        except ValueError:
            print("Digite uma opção válida")
    exit("Limite de tentativas atingido.")


def add_item(quantity="1"):
    """
    Adiciona um item à lista de compras.
    O usuário é solicitado a fornecer o nome do produto e a quantidade.
    Se o usuário inserir uma quantidade inválida, ele terá três tentativas antes de retornar à função principal.
    O usuário tem a opção de adicionar mais produtos à lista.
    """
    product = input("Digite o produto que deseja adicionar: ")
    for i in range(3):
        quantity_inputed = input("digite a quantidade do produto, ou tecle enter para adicionar 1: ")
        try:
            match quantity_inputed:
                case "" | "1":
                    break
                case "0":
                    raise ValueError
                case _:
                    quantity = int(quantity_inputed)
                    break
        except ValueError:
            print("Digite um valor válido.")
            if i == 2:
                print("Número de tentativas excedido.")
                main()
    shopping_cart.update({product: quantity})
    if input("Deseja adicionar mais produtos? ").lower() in ["s", "ss", "sim"]:
        add_item()
    main()


def remove_item():
    """
    Remove um item da lista de compras.
    Se o produto não estiver na lista, o usuário terá a opção de tentar novamente.
    Se em três tentativas o produto não for encontrado, o usuário será redirecionado para a função principal.
    """
    for i in range(3):
        try:
            product = input("Digite o produto que deseja remover: ")
            if product not in shopping_cart:
                raise ValueError
            shopping_cart.pop(product)
            print(f"Produto {product} removido com sucesso.")
            if input("Deseja remover mais produtos? ").lower() in ["s", "ss", "sim"]:
                remove_item()
            main()
        except ValueError:
            if input("Produto não encontrado. Tentar novamente? ").lower() in ["n", "não"]:
                main()
    print("numero de tentativas excedido.")
    main()


def edit_quantity():
    """
    Edita a quantidade de um item na lista de compras.
    Se o produto não estiver na lista, o usuário terá a opção de tentar novamente.
    Se o usuário inserir uma quantidade inválida, ele terá três tentativas antes de retornar à função principal.
    """
    product = input("Digite o produto que deseja editar a quantidade: ")
    if product not in shopping_cart:
        print("Produto não encontrado.")
        if input("Deseja tentar novamente? ").lower() in ["s", "ss", "sim"]:
            edit_quantity()
        main()

    for i in range(3):
        try:
            quantity = int(input("Digite a nova quantidade: "))
            shopping_cart[product] = quantity
            print(f"Quantidade de {product} atualizada para {quantity}")
            if input("Deseja editar mais produtos? ").lower() in ["s", "ss", "sim"]:
                edit_quantity()
            main()
        except ValueError:
            print("Digite um valor inteiro.")
    print("Número de tentativas excedido.")
    main()


def view_shopping_list(**kwargs):
    """
    Exibe a lista de compras atual.
    Se a lista estiver vazia, informa ao usuário que a lista de compras está vazia.
    """
    if not kwargs:
        print("Lista de compras vazia.")
        main()
    print("Aqui está sua lista de compras:\n")
    for product, quantity in kwargs.items():
        print(f"{quantity}x {product}")
    main()


def main():
    """
    Chama a função select_actions() e processa o valor retornado para definir a ação a ser executada.
    """
    match select_actions():
        case "1":
            add_item()
        case "2":
            remove_item()
        case "3":
            edit_quantity()
        case "4":
            view_shopping_list(**shopping_cart)
            main()
        case "5":
            exit("Programa encerrado.")


if __name__ == '__main__':
    main()
