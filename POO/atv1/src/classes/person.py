class Person:

    def __init__(self, name, birth, email):
        self.__name = name
        self.__birth = birth
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, birth):
        self.__birth = birth

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def show_person_data(self):
        print(f'Nome: {self.name}')
        print(f'Data de nascimento: {self.birth}')
        print(f'Email: {self.email}')
