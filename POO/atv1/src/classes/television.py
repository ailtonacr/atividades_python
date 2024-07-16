from random import randint


def number_generator(initial_value=0, final_value=100):
    return randint(initial_value, final_value)


class Television:
    def __init__(self):
        self.__status = False
        self.__volume = number_generator()
        self.__chanel = number_generator()

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if 0 <= volume <= 100:
            self.__volume = volume

    @property
    def chanel(self):
        return self.__chanel

    @chanel.setter
    def chanel(self, chanel):
        if chanel > 0:
            self.__chanel = chanel

    def on(self):
        self.status = True
        print('Tv ligada.')

    def off(self):
        self.status = False
        print('Tv desligada')

    def upper_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f'Volume aumentado para: {self.volume}')

    def lower_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f'Volume diminuído para: {self.volume}')

    def upper_chanel(self):
        self.chanel += 1
        print(f'Canal mudou para: {self.chanel}')

    def lower_chanel(self):
        if self.chanel > 1:
            self.chanel -= 1
            print(f'Canal mudou para: {self.chanel}')

    def __set_chanel(self, chanel):
        if chanel > 0:
            self.chanel = chanel
            print(f'Canal mudou para: {self.chanel}')

    def change_channel(self):
        try:
            chanel = int(input('Digite o canal que deseja assistir: '))
            self.__set_chanel(chanel)
        except ValueError:
            print('Canal inválido!')


class RemoteControl:
    def __init__(self, television):
        self.television = television

    def on(self):
        self.television.on()

    def off(self):
        self.television.off()

    def upper_volume(self):
        self.television.upper_volume()

    def lower_volume(self):
        self.television.lower_volume()

    def upper_chanel(self):
        self.television.upper_chanel()

    def lower_chanel(self):
        self.television.lower_chanel()

    def change_channel(self):
        self.television.change_channel()
