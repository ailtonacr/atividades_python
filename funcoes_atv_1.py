"""
Atividade: Sistema de Gerenciamento de Livros
Você vai criar um sistema simples de gerenciamento de livros. O sistema permitirá adicionar livros, listar todos os livros,
buscar livros por título, e calcular o valor total de todos os livros em estoque.

Passo 1:
Defina uma função principal main que será responsável por chamar as outras funções.

Passo 2:
Crie uma função adicionar_livro que recebe o título do livro, autor, ano de publicação e preço como parâmetros.
Armazene essas informações em uma lista de dicionários.

Passo 3:
Crie uma função listar_livros que exibe todos os livros adicionados.

Passo 4:
Crie uma função buscar_livro que recebe um título ou id como parâmetro e retorna o livro correspondente.

Passo 5:
Crie uma função calcular_valor_total que retorna a soma dos preços de todos os livros.

Passo 6:
Adicione docstrings a todas as funções explicando o que cada uma faz.

Passo 7:
Adicione uma função adicionar_varios_livros que permite adicionar vários livros de uma vez.

Adicionei o o campo id para cada livro adicionado como auto increment, para facilitar uma possivel busca por id.

"""
from sys import exit
from datetime import date

books_inventory = []


def select_actions():
    """
    Função para selecionar a ação a ser realizada.
    :return: retorna o numero correspondente à ação selecionada
    """
    for i in range(3):
        try:
            action = input("Selecione uma opção:\n"
                           "1. adicionar livros\n"
                           "2. listar livros\n"
                           "3. buscar livros por título ou id\n"
                           "4. calcular valor total dos livros\n"
                           "5. adicionar vários livros\n"
                           "6. sair\n"
                           )
            if int(action) not in range(1, 6):
                raise ValueError
            return action
        except ValueError:
            print("Digite uma opção válida")
            return select_actions()
    exit("Limite de tentativas atingido.")


def add_book():
    """
    Adiciona um novo livro ao inventário.
    :return: retorna para a função main
    """
    title = input("Digite o título do livro: ")
    author = input("Digite o autor do livro: ")
    for i in range(3):
        try:
            publication_year = int(input("Digite o ano de publicação do livro: "))
            if publication_year < 0 or publication_year > date.today().year or len(str(publication_year)) != 4:
                raise ValueError
            break
        except ValueError:
            print("Digite um ano válido.")
            if i == 2:
                return main()
    price = float(input("Digite o preço do livro: ").replace(',', '.'))
    for i in range(3):
        try:
            quantity = int(input("Digite a quantidade de livros: "))
            if quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("Digite um valor válido.")
            if i == 2:
                return main()
    books_inventory.append(
        {
            "id": len(books_inventory) + 1,
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "price": price,
            "quantity": quantity
        }
    )
    print("Livro adicionado ao inventário com sucesso!\n")


def list_books():
    """
    Lista todos os livros cadastrados.
    :return: retorna para a função main
    """
    if len(books_inventory) > 0:
        for book in books_inventory:
            print(f"ID: {book['id']}\n"
                  f"Titulo: {book['title']}\n"
                  f"Autor: {book['author']}\n"
                  f"Ano de publicação: {book['publication_year']}\n"
                  f"Valor unitário: {book['price']:.2f}\n"
                  f"Quantidade: {book['quantity']}\n"
                  )
        return main()
    print("Nenhum livro cadastrado.")
    return main()


def search_books():
    """
    Busca um livro pelo título ou id.
    :return: retorna para a função main
    """
    search = input("Digite o título ou id do livro que deseja buscar: ").lower()
    for book in books_inventory:
        if book['title'].lower() or book['id'] == search:
            print(f"ID: {book['id']}\n"
                  f"Titulo: {book['title']}\n"
                  f"Autor: {book['author']}\n"
                  f"Ano de publicação: {book['publication_year']}\n"
                  f"Valor unitário: {book['price']:.2f}\n"
                  f"Quantidade: {book['quantity']}\n"
                  )
            return main()
    print("Livro não encontrado.")
    return main()


def calculate_total_value():
    """
    Calcula a soma total dos valores dos livros em estoque e printa o total.
    :return: retorna o valor total dos livros em estoque
    """
    total_value = 0
    if len(books_inventory) == 0:
        print("Nenhum livro cadastrado.")
        return main()
    for book in books_inventory:
        total_value += book['price'] * book['quantity']
    print(f"Você possui um total de {len(books_inventory)} livros em seu estoque.\n"
          f"O valor total dos livros em estoque é de R${total_value:.2f}")
    return main()


def add_multiple_books():
    """
    Adiciona vários livros ao inventário.
    :return: retorna para a função main
    """
    while True:
        add_book()
        if input("Deseja adicionar mais livros? (s/n): ").strip().lower() == 'n' or 'nao' or 'não' or 'no' or 'nope':
            return main()


def main():
    """
    Função principal que chama as outras funções.
    """
    match select_actions():
        case "1":
            add_book()
            return main()
        case "2":
            list_books()
            return main()
        case "3":
            search_books()
            return main()
        case "4":
            calculate_total_value()
            return main()
        case "5":
            add_multiple_books()
            return main()
        case "6":
            exit("Obrigado por utilizar o nosso sistema de gerenciamento de livros!")


if __name__ == '__main__':
    main()
