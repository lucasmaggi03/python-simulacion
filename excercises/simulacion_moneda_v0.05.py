import random 
import sys 


if len(sys.argv) != 3 or sys.argv[1] != "-n":
    print("Uso: python simulacion_moneda_v0.05.py -n <num_valores>")
    sys.exit(1)
num_valores = int(sys.argv[2])
valores = [random.randint(0,1) for _ in range(num_valores)]
print("Valores generados: ", valores)