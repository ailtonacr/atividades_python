class Contact:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    def __str__(self):
        return f'"Nome": {self.name}, "Telefone": {self.phone}'


class ContactBook:

    def __init__(self):
        self.__contacts = []

    def stock_contact(self, contact):
        self.__contacts.append(contact)

    def remove_contact(self, contact):
        if contact in self.__contacts:
            self.__contacts.remove(contact)

    def search_contact(self, name):
        for i, contact in enumerate(self.__contacts):
            if contact.name == name:
                return i
        return -1

    def show_contact_book(self):
        for contact in self.__contacts:
            print(contact)

    def print_contact_by_index(self, index):
        if 0 <= index < len(self.__contacts):
            print(self.__contacts[index])
        else:
            print("Índice inválido!")
