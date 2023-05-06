class Coctel:
    def __init__(self, nombre, precio, grados_alcohol):
        self.nombre = nombre
        self.precio = precio
        self.grados_alcohol = grados_alcohol
    
    def calcular_costo(self, cantidad):
        pass
    
    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio
    
    def get_grados_alcohol(self):
        return self.grados_alcohol
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_precio(self, precio):
        self.precio = precio
    
    def set_grados_alcohol(self, grados_alcohol):
        self.grados_alcohol = grados_alcohol