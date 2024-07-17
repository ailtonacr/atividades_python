class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'"Nome": {self.name}, "Telefone": {self.phone}'


class ContactBook:

    def __init__(self):
        self.contacts = []

    def stock_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        index = self.search_contact(name)
        if index != -1:
            del self.contacts[index]

    def search_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                return i
        return -1

    def show_contact_book(self):
        for contact in self.contacts:
            print(contact)

    def print_contact_by_index(self, index):
        if 0 <= index < len(self.contacts):
            print(self.contacts[index])
        else:
            print("Índice inválido!")
