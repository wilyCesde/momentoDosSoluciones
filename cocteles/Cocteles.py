class Cocteles:
    def __init__(self):
        self.nombre = None
        self.precio = None
        self.gradosAlcohol = None

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, dato):
        self.__precio = dato

    @property
    def gradosAlcohol(self):
        return self.__gradosAlcohol

    @gradosAlcohol.setter
    def gradosAlcohol(self, dato):
        self.__gradosAlcohol = dato
