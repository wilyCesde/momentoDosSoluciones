from Escuderia import Escuderia

escuderias = []
contador = 1

numeroEscuderias = int(input('Digite el número de escuderías: '))

while contador <= numeroEscuderias:
    print(f'ESCUDERÍA #{contador}')
    escuderia = Escuderia()

    escuderia.nombre = input('Digite el nombre de la escudería: ')
    escuderia.casaMotor = input('Digite el nombre de la casa motor: ')

    escuderia.pilotoPrincipal.nombre = input('Digite el nombre del primer piloto: ')
    escuderia.pilotoPrincipal.salarioAnual = int(input(f'Digite el salario de {escuderia.pilotoPrincipal.nombre}: '))
    escuderia.pilotoPrincipal.fechaNacimiento = input(f'Digite la fecha de nacimiento de {escuderia.pilotoPrincipal.nombre}: ')
    escuderia.pilotoPrincipal.pais = input(f'Digite el país de {escuderia.pilotoPrincipal.nombre}: ')

    escuderia.piloto2.nombre = input('Digite el nombre del segundo piloto: ')
    escuderia.piloto2.salarioAnual = int(input(f'Digite el salario de {escuderia.piloto2.nombre}: '))
    escuderia.piloto2.fechaNacimiento = input(f'Digite la fecha de nacimiento de {escuderia.piloto2.nombre}: ')
    escuderia.piloto2.pais = input(f'Digite el país de {escuderia.piloto2.nombre}: ')

    escuderia.costos = int(input(f'Digite el valor de los costos de {escuderia.nombre}: '))

    escuderias.append(escuderia)
    contador += 1


costoMayor = 0
nombreEscuderiaMasCara = None

for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
        nombreEscuderiaMasCara = escuderia.nombre

print(f'La escudería más cara es {nombreEscuderiaMasCara} con un costo anual de {costoMayor}')
