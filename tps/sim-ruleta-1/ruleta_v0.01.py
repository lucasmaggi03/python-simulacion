import random 
import matplotlib.pyplot as plt
import numpy as np
import sys


num_corridas = int(sys.argv[3])
num_elegido = int(sys.argv[2])
cant_tiradas = int(sys.argv[1])
valores_corrida = []
suma_total_corridas = []
valor_varianza_corrida = []

fig, axs = plt.subplots(2, 2, figsize=(18, 6))
for j in range(num_corridas):
    suma_total = 0
    cant_victorias = 0
    frecuencia_relativa_victorias = []
    valor_promedio_respecto_n = []
    valor_varianza = []
    valor_desvio = []


    valores = [random.randint(0,36) for i in range(cant_tiradas)]
    for i in range(cant_tiradas):
        if(valores[i] == num_elegido):
            cant_victorias += 1
        frecuencia_relativa_victorias.append(cant_victorias / (i+1))
        suma_total = suma_total + valores[i]
        valor_promedio_respecto_n.append(suma_total/(i+1))
        valor_varianza.append(np.var(valores[:i+1]))
        valor_desvio.append(np.std(valores[:i+1]))
    
    valores_corrida.append(valores)
    suma_total_corridas.append(suma_total)

    axs[0][0].plot(frecuencia_relativa_victorias, label=f"Frecuencia relativa de victorias en la corrida {j+1}")
    axs[0][0].set_xlabel('Número de tiradas')
    axs[0][0].set_ylabel('Frecuencia Relativa')
    axs[0][0].set_title(f'Frecuencia Relativa del número {num_elegido} en {cant_tiradas} tiradas')
    axs[0][1].plot(valor_promedio_respecto_n, label=f"Valor promedio N en la corrida {j+1}")
    axs[0][1].set_xlabel('Número de tiradas')
    axs[0][1].set_ylabel('Promedio de las Tiradas')
    axs[0][1].set_title(f'Promedio de los numeros en {cant_tiradas} tiradas')
    axs[1][0].plot(valor_varianza, label=f"Valor varianza N en la corrida {j+1}")
    axs[1][0].set_xlabel("Número de tiradas")
    axs[1][0].set_ylabel('Varianza')
    axs[1][0].set_title(f'Varianza en {cant_tiradas} tiradas')
    axs[1][1].plot(valor_desvio, label=f"Valor desvio estandar N en la corrida {j+1}")
    axs[1][1].set_xlabel("Número de tiradas")
    axs[1][1].set_ylabel('Desvío Estandar')
    axs[1][1].set_title(f'Desvío estandar en {cant_tiradas} tiradas')
    plt.tight_layout()
axs[0][0].axhline(y=1/37, color='red', linestyle='--', label="Frecuencia relativa esperada corrida")
axs[0][1].axhline(y=(sum(suma_total_corridas)/(cant_tiradas*num_corridas)), color='red', linestyle='--', label="Frecuencia relativa esperada corrida")
axs[1][0].axhline(y=np.var(valores_corrida), color='red', linestyle='--', label="Valor varianza esperada")
axs[1][1].axhline(y=np.std(valores_corrida), color='red', linestyle='--', label="Valor desviacion estandar esperada")
plt.savefig("Graficas.png")
plt.show()