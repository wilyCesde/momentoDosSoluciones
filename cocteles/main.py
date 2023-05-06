from CoctelFrutas import CoctelFrutas
from ShotDeAlcohol import ShotDeAlcohol

def calcular_costo_venta(tipo_producto, cantidad, precio_unitario, annejo=None):
    costo = 0
    if tipo_producto == 'Shot':
        costo = cantidad * precio_unitario
    elif tipo_producto == 'Coctel':
        if annejo == 1:
            costo = cantidad * precio_unitario
        elif annejo == 2:
            costo = cantidad * precio_unitario * 0.8
        elif annejo == 3:
            costo = cantidad * precio_unitario * 0.5
        elif annejo == 4:
            print('No se puede vender un coctel añejado por más de 3 días.')
        else:
            print('El valor de añejamiento debe estar entre 1 y 4.')
    return costo

total_venta = 0

while True:
    tipo_producto = input('Digite el tipo de producto (Shot o Coctel): ')
    if tipo_producto == 'Shot':
        shot = ShotDeAlcohol()
        cantidad = int(input('Digite la cantidad de productos: '))
        precio_unitario = float(input('Digite el precio unitario del Shot: '))
        shot.temperatura = input('Digite la temperatura a la que se sirvió el Shot: ')
        costo = calcular_costo_venta(tipo_producto, cantidad, precio_unitario)
        total_venta += costo
        print(f"Costo de {cantidad} Shots a {precio_unitario} cada uno: ${costo}")
    elif tipo_producto == 'Coctel':
        nombre = input('Digite el nombre del coctel: ')
        precio_unitario = float(input('Digite el precio unitario del coctel: '))
        grados_alcohol = float(input('Digite los grados de alcohol del coctel: '))
        nivel_frescura = input('Digite el nivel de frescura del coctel (fresco/estable): ')
        coctel_frutas = CoctelFrutas(nombre, precio_unitario, grados_alcohol, nivel_frescura)
        cantidad = int(input('Digite la cantidad de productos: '))
        annejo = int(input('Digite la cantidad de días de añejamiento (1-3): '))
        costo = calcular_costo_venta(tipo_producto, cantidad, precio_unitario, annejo)
        total_venta += costo
        print(f"Costo de {cantidad} {nombre} con {nivel_frescura} nivel de frescura y {grados_alcohol} grados de alcohol, añejado por {annejo} días, a {precio_unitario} cada uno: ${costo}")
    else:
        print('El tipo de producto debe ser Shot o Coctel.')
    
    continuar = input('¿Desea agregar otro producto? (si/no): ')
    if continuar == 'no':
        break

print(f"Total de la venta: ${total_venta}")
