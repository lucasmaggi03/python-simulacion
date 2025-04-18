import random 
import matplotlib.pyplot as plt
import sys


num_corridas = int(sys.argv[3])
num_elegido = int(sys.argv[2])
cant_tiradas = int(sys.argv[1])
colores = ["red", "green", "blue"]

fig, axs = plt.subplots(1, 2, figsize=(18, 6))
axs[0].axhline(y=1/37, color='red', linestyle='--', label="Frecuencia relativa esperada corrida")
axs[1].axhline(y=18, color='red', linestyle='--', label="Frecuencia relativa esperada corrida")
for j in range(num_corridas):
    cant_victorias = 0
    suma_total = 0
    frecuencia_relativa_victorias = []
    frecuencia_absoluta_victorias = []
    valor_promedio_respecto_n = []


    valores = [random.randint(0,36) for i in range(cant_tiradas)]
    for i in range(cant_tiradas):
        if(valores[i] == num_elegido):
            cant_victorias += 1
        frecuencia_relativa_victorias.append(cant_victorias / cant_tiradas)
        frecuencia_absoluta_victorias.append(cant_victorias)
        suma_total = suma_total + valores[i]
        valor_promedio_respecto_n.append(suma_total/cant_tiradas)

    valor_promedio = suma_total / cant_tiradas

    print("Valores: ")
    print(valores)
    print("Numero elegido: ")
    print(num_elegido)
    print("Cant. de victorias: ")
    print(cant_victorias)
    print("Frecuencia relativa de victorias: ")
    print(frecuencia_relativa_victorias)
    print("Frecuencia absoluta de victorias: ")
    print(frecuencia_absoluta_victorias)

    axs[0].plot(frecuencia_relativa_victorias, label=f"Frecuencia relativa victorias corrida {j+1}", color=colores[j])
    axs[0].set_xlabel("Número de tiradas")
    axs[0].set_ylabel("Frecuencia relativa")
    axs[0].set_title("Grafica de Valores")
    axs[1].plot(valor_promedio_respecto_n, label=f"Frecuencia relativa victorias corrida {j+1}", color=colores[j])
    axs[1].set_xlabel("Número de tiradas")
    axs[1].set_ylabel("Valor promedio de las tiradas")
    axs[1].set_title("Grafica de Valores")
    plt.tight_layout()
plt.show()