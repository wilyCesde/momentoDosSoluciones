from Coctel import Coctel


class ShotDeAlcohol(Coctel):
    def __init__(self, nombre, precio, grados_alcohol, temperatura):
        super().__init__(nombre, precio, grados_alcohol)
        self.temperatura = temperatura
    
    def calcular_costo(self, cantidad):
        return cantidad * self.precio
    
    def get_temperatura(self):
        return self.temperatura
    
    def set_temperatura(self, temperatura):
        self.temperatura = temperatura