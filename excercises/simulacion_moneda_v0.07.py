import random
import sys 

if len(sys.argv) != 3 or sys.argv[1] != "-n":
    print("Uso: python simulacion_moneda_v0.06.py -n <num_valores>")
    sys.exit(1)
num_valores = int(sys.argv[2])
frecuencia_absoluta_0 = frecuencia_absoluta_1 = 0
for _ in range(num_valores):
    nuevo_valor = random.randint(0,1)
    if nuevo_valor == 0:
        frecuencia_absoluta_0 += 1
    else:
        frecuencia_absoluta_1 += 1
    total_valores = frecuencia_absoluta_0 + frecuencia_absoluta_1
    frecuencia_relativa_0 = frecuencia_absoluta_0 / total_valores
    frecuencia_relativa_1 = frecuencia_absoluta_1 / total_valores
    print(f"Valor generado: {nuevo_valor}")
    print(f"Frecuencia absoluta de 0: {frecuencia_absoluta_0}")
    print(f"Frecuencia relativa de 0: {frecuencia_relativa_0}")
    print(f"Frecuencia absoluta de 1: {frecuencia_absoluta_1}")
    print(f"Frecuencia relativa de 1: {frecuencia_relativa_1}")
    print()
