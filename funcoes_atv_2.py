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

shopping_list = {}


def select_actions():
    """
    Solicita ao usuário que selecione uma ação.
    Se o usuário inserir uma opção inválida, ele terá três tentativas antes de o programa ser encerrado.
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
            return select_actions()
    exit("Limite de tentativas atingido.")


def add_item(quantity="1"):
    """
    Adiciona um item à lista de compras.
    O usuário é solicitado a fornecer o nome do produto e a quantidade.
    Se o usuário inserir uma quantidade inválida, ele terá três tentativas antes de retornar à função principal.
    O usuário tem a opção de adicionar mais produtos à lista.
    """
    products = input("Digite o produto que deseja adicionar: ")
    for i in range(3):
        try:
            quantity_inputed = input("digite a quantidade do produto, ou tecle enter para adicionar 1: ")
            if quantity_inputed == "":
                pass
            elif quantity_inputed.isnumeric() is True:
                quantity = quantity_inputed
            else:
                raise ValueError
            break
        except ValueError:
            print("Digite um valor válido.")
            if i == 2:
                print("Número de tentativas excedido.")
                return main()
    shopping_list.update({products: quantity})
    if input("Deseja adicionar mais produtos? (s/n): ") == "s":
        return add_item()
    return main()


def remove_item():
    """
    Remove um item da lista de compras.
    Se o produto não estiver na lista, o usuário terá a opção de tentar novamente.
    Se em três tentativas o produto não for encontrado, o usuário será redirecionado para a função principal.
    """
    for i in range(3):
        try:
            product_to_remove = input("Digite o produto que deseja remover: ")
            if product_to_remove not in shopping_list.keys():
                raise ValueError
            shopping_list.pop(product_to_remove)
            print(f"Produto {product_to_remove} removido com sucesso.")
            if input("Deseja remover mais produtos? (s/n): ") == "s":
                return remove_item()
            return main()
        except ValueError:
            if input("Produto não encontrado. Tentar novamente? (s/n): ") in ["n", "não"]:
                return main()
    print("numero de tentativas excedido.")
    return main()


def edit_quantity():
    """
    Edita a quantidade de um item na lista de compras.
    Se o produto não estiver na lista, o usuário terá a opção de tentar novamente.
    Se o usuário inserir uma quantidade inválida, ele terá três tentativas antes de retornar à função principal.
    """
    product_to_edit = input("Digite o produto que deseja editar a quantidade: ")
    if product_to_edit not in shopping_list:
        print("Produto não encontrado.")
        if input("Deseja tentar novamente? (s/n): ").lower() in ["s", "sim"]:
            return edit_quantity()
        return main()

    for i in range(3):
        try:
            new_quantity = int(input("Digite a nova quantidade: "))
            shopping_list[product_to_edit] = new_quantity
            print(f"Quantidade de {product_to_edit} atualizada para {new_quantity}")
            if input("Deseja editar mais produtos? (s/n): ").lower() == "s":
                return edit_quantity()
            return main()
        except ValueError:
            print("Digite um valor inteiro.")
            if i == 2:
                print("Número de tentativas excedido.")
                return main()
    return main()


def view_shopping_list(**kwargs):
    """
    Exibe a lista de compras atual.
    Se a lista estiver vazia, informa ao usuário que a lista de compras está vazia.
    """
    if not kwargs:
        print("Lista de compras vazia.")
        return main()
    print("Aqui está sua lista de compras:\n")
    for product, quantity in kwargs.items():
        print(f"{quantity}x {product}")
    return main()


def main():
    """
    Função principal que chama as outras funções com base na ação selecionada pelo usuário.
    """
    match select_actions():
        case "1":
            add_item()
        case "2":
            remove_item()
        case "3":
            edit_quantity()
        case "4":
            view_shopping_list(**shopping_list)
            return main()
        case "5":
            exit("Programa encerrado.")


if __name__ == '__main__':
    main()
