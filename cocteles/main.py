from Coctel import Coctel
from CoctelConJugoDeFrutas import CoctelConJugoDeFrutas
from ShotDeAlcohol import ShotDeAlcohol

# coctel = Coctel()

coctel1 = CoctelConJugoDeFrutas("Piña Colada", 8, 10, "fresco")
coctel2 = CoctelConJugoDeFrutas("Margarita", 7, 8, "2 días")
coctel3 = ShotDeAlcohol("Tequila", 5, 40, "frío")

venta = [coctel1, coctel2, coctel3]

total_venta = 0
for coctel in venta:
 cantidad = int(input(f"Ingrese la cantidad de {coctel.get_nombre()}: "))
 costo = coctel.calcular_costo(cantidad)
total_venta += costo
print(f"Costo de {cantidad} {coctel.get_nombre()}: ${costo}")

print(f"Total de la venta: ${total_venta}")