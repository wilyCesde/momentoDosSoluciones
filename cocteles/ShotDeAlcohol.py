from Cocteles import Cocteles
class ShotDeAlcohol(Cocteles):
    def __init__(self):
        self.temperatura = None

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, dato):
        self.__temperatura = dato