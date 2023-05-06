
from Coctel import Coctel


class CoctelConJugoDeFrutas(Coctel):
    def __init__(self, nombre, precio, grados_alcohol, nivel_frescura):
        super().__init__(nombre, precio, grados_alcohol)
        self.nivel_frescura = nivel_frescura
    
    def calcular_costo(self, cantidad):
        if self.nivel_frescura == "fresco":
            return cantidad * self.precio
        else:
            return 0

