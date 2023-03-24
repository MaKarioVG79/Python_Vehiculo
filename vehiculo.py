class vehiculo():
    color = "Azul"
    ruedas = 4
    puertas = 2


class coche(vehiculo):
    velocidad = 100
    cilindrada = 8

coche.matricula = "A456T7B"

print("El color es: ", coche.color)
print("La velocidad es: ", coche.velocidad)
print("La matricula es: ", coche.matricula)




