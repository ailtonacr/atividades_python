"""
1. Crie uma classe "Person", contendo "name", "birth" e "email". Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.

2. Crie uma classe "ContactBook" que pode armazenar contatos e seja possível realizar as seguintes operações:
a) stock_contact(contact: ContactBook); // Adiciona um contato na agenda.
b) remove_contact(contact: ContactBook); // Remove um contato da agenda.
c) search_contact(name: str); // Informa em que posição da agenda está o contato.
d) show_contact_book(); // Imprime os dados de todos os contatos da agenda.
e) print_contact_by_index(index: int); // Imprime os dados do contato informado pelo índice.

3. Crie as classes "Television" com atributo "status", "volume", "chanel" e "Control" com o atributo "television", de
forma que possamos ligar, desligar e gerenciar som e canais tanto via "television" quanto via "remote control".
a) on(), off() // Permitem ligar e desligar a televisão;
b) upper_volume(), lower_volume() // Permitem aumentar ou diminuir o volume de som em uma unidade de cada vez;
c) upper_chanel(), lower_chanel() // Permitem aumentar ou diminuir o canal em uma unidade de cada vez;
d) change_channel() // Permite informar um número de canal para efetuar a troca.
"""
from classes import Person, ContactBook, Contact, Television, RemoteControl


if __name__ == '__main__':

    # 1
    rafael = Person('Rafael', '24/09/2002', 'rafael@example.com')
    rafael.show_person_data()

    # 2
    ailton: Contact = Contact("Ailton", "21 99999-9999")
    bruno: Contact = Contact("Bruno", "22 99999-9999")
    cecilia: Contact = Contact("Cecilia", "23 99999-9999")

    schedule = ContactBook()
    schedule.stock_contact(ailton)
    schedule.stock_contact(bruno)
    schedule.stock_contact(cecilia)

    print("Agenda completa:")
    schedule.show_contact_book()

    search_name: str = "bruno"
    index: int = schedule.search_contact(search_name)
    print(f"\nResultado da busca por '{search_name}':")
    schedule.print_contact_by_index(index)

    schedule.remove_contact(bruno)
    print("\nAgenda após remover Bruno:")
    schedule.show_contact_book()

    # 3
    tv = Television()

    tv.on()
    tv.upper_volume()
    tv.lower_volume()
    tv.upper_chanel()
    tv.lower_chanel()
    tv.change_channel()
    tv.off()
    print('\n')

    control = RemoteControl(tv)

    control.on()
    control.upper_volume()
    control.lower_volume()
    control.upper_chanel()
    control.lower_chanel()
    control.change_channel()
    control.off()
