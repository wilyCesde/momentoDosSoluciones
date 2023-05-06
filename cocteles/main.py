from Cocteles import Cocteles
from CoctelFrutas import CoctelFrutas
from ShotDeAlcohol import ShotDeAlcohol

coctel = Cocteles()

total_venta = 0

tipoProducto = input('Digite el tipo de producto (Shot o Coctel): ')
cantidad = int(input('Digite la cantidad de productos: '))
coctel.__precio = float(input(f'Digite el precio de {tipoProducto}'))

if (tipoProducto == 'Shot'):
    costo = cantidad * coctel.precio
elif (tipoProducto == 'Coctel'):
    annejo = int(input('Cantidad de añejamiento (1 - 1 Dia, 2 - 2 Dias, 3 - 3 Dias, 4 - Más de tres días): '))

    if annejo == 1:
        costo = cantidad * coctel.precio
    elif annejo == 2:
        costo = (cantidad * coctel.precio) - 0.2
    elif annejo == 3:
        costo = (cantidad * coctel.precio) - 0.5
    elif annejo == 4:
        print('No hay venta. Paila')
    else:
        print('Entre 1 y 4')

# for coctel in venta:
#  cantidad = int(input(f"Ingrese la cantidad de {coctel.get_nombre()}: "))
#  costo = coctel.calcular_costo(cantidad)
# total_venta += costo
# print(f"Costo de {cantidad} {coctel.get_nombre()}: ${costo}")

# print(f"Total de la venta: ${total_venta}")
