import random 
import matplotlib.pyplot as plt
import numpy as np
import sys


num_corridas = int(sys.argv[3])
num_elegido = int(sys.argv[2])
cant_tiradas = int(sys.argv[1])
colores = ["red", "green", "blue"]
valores_corrida = []
suma_total_corridas = []
valor_varianza_corrida = []

fig, axs = plt.subplots(1, 4, figsize=(18, 6))
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
        frecuencia_relativa_victorias.append(cant_victorias / cant_tiradas)
        suma_total = suma_total + valores[i]
        valor_promedio_respecto_n.append(suma_total/cant_tiradas)
        valor_varianza.append(np.var(valores[:i+1]))
        valor_desvio.append(np.std(valores[:i+1]))
    
    valores_corrida.append(valores)
    suma_total_corridas.append(suma_total)

    axs[0].plot(frecuencia_relativa_victorias, label=f"Frecuencia relativa de victorias en la corrida {j+1}", color=colores[j])
    axs[0].set_xlabel("Número de tiradas")
    axs[0].set_ylabel("Frecuencia relativa de victorias")
    axs[0].set_title("Grafica de Frecuencias relativas de victorias")
    axs[1].plot(valor_promedio_respecto_n, label=f"Valor promedio N en la corrida {j+1}", color=colores[j])
    axs[1].set_xlabel("Número de tiradas")
    axs[1].set_ylabel("Valor promedio de las tiradas")
    axs[1].set_title("Grafica de Valores promedio entre las corridas")
    axs[2].plot(valor_varianza, label=f"Valor varianza N en la corrida {j+1}", color=colores[j])
    axs[2].set_xlabel("Número de tiradas")
    axs[2].set_ylabel("Valor de varianza")
    axs[2].set_title("Grafica de varianza entre las corridas")
    axs[3].plot(valor_desvio, label=f"Valor desvio estandar N en la corrida {j+1}", color=colores[j])
    axs[3].set_xlabel("Número de tiradas")
    axs[3].set_ylabel("Valor de desvio estandar")
    axs[3].set_title("Grafica de desvio estandar entre las corridas")
    plt.tight_layout()
axs[0].axhline(y=1/37, color='red', linestyle='--', label="Frecuencia relativa esperada corrida")
axs[1].axhline(y=(sum(suma_total_corridas)/(cant_tiradas*num_corridas)), color='red', linestyle='--', label="Frecuencia relativa esperada corrida")
plt.show()