"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.

2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de
forma que:
a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também
permitir que seja informado um número de canal para efetuar a troca;
"""
from classes import Person, Schedule, Contact, Television, Control


if __name__ == '__main__':

    # 1
    ailton = Person('Ailton', '24/09/2002', 'ailton@example.com')
    ailton.print_person()

    # 2
    ailton = Contact("Ailton", "21 99999-9999")
    bruno = Contact("Bruno", "22 99999-9999")
    cecilia = Contact("Cecilia", "23 99999-9999")

    schedule = Schedule()
    schedule.stock_contact(ailton)
    schedule.stock_contact(bruno)
    schedule.stock_contact(cecilia)

    print("Agenda completa:")
    schedule.print_schedule()

    search_name = "bruno"
    index = schedule.search_contact(search_name)
    print(f"\nResultado da busca por '{search_name}':")
    schedule.print_contact_index(index)

    schedule.remove_contact(bruno)
    print("\nAgenda após remover Bruno:")
    schedule.print_schedule()

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

    remote = Control(tv)

    remote.on()
    remote.upper_volume()
    remote.lower_volume()
    remote.upper_chanel()
    remote.lower_chanel()
    remote.change_channel()
    remote.off()
