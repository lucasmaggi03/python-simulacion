import random
import sys

while True:
    try:
        num = int(input("Cant. de lanzamientos: "))
        if num <= 0:
            print("Por favor, ingrese un número entero positivo.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

contador = 0
cara = 0
cruz = 0

while contador < num:
    resultado = random.randint(0, 1)
    if resultado == 0:
        cara += 1
    else:
        cruz += 1
    contador += 1

print("Cara: ", cara)
print("Cruz: ", cruz)