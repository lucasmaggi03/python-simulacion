import random 
import matplotlib.pyplot as plt
import numpy as np
import sys

tipo_capital = sys.argv[5]
estrategia_elegida = sys.argv[4]
num_corridas = int(sys.argv[3])
num_elegido = int(sys.argv[2])
cant_tiradas = int(sys.argv[1])
valores_corrida = []
montos_cajas_corrida = []


numeros_rojos = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
numeros_negros = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
numeros_columnas = [[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36]]
numeros_filas = [[1,4,7,10,13,16,19,22,25,28,31,34],[2,5,8,11,14,17,20,23,26,29,32,35],[3,6,9,12,15,18,21,24,27,30,33,36]]


fig, axs = plt.subplots(1, 2, figsize=(18, 6))
axs[0].axhline(y=10000, color='red', linestyle='--', label="Monto de caja inicial")
for j in range(num_corridas):
    #Elegimos el monto caja inicial de 10000 U.M.
    monto_caja_actual = 10000
    valores = [random.randint(0,36) for i in range(cant_tiradas)]
    valores_corrida.append(valores)
    monto_caja = []


    if (estrategia_elegida == "m"):
        apuesta_m = 10
        # Elegimos el color ROJO para hacer la prueba
        for i in range(cant_tiradas):
            if(((monto_caja_actual - apuesta_m) < 0) and (tipo_capital == "f")):
                break
            if(valores[i] in numeros_rojos):
                monto_caja_actual = monto_caja_actual + apuesta_m
                apuesta_m = 10
            else:
                monto_caja_actual = monto_caja_actual - apuesta_m
                apuesta_m = apuesta_m*2
            monto_caja.append(monto_caja_actual)
            print(monto_caja)


    if  (estrategia_elegida == "f"):
        # Elegimos el color ROJO para hacer la prueba
        f1 = 0
        f2 = 1
        apuesta_f = f1 + f2
        for i in range(cant_tiradas):
            if(((monto_caja_actual - apuesta_f) < 0) and (tipo_capital == "f")):
                break
            if(valores[i] in numeros_rojos):
                monto_caja_actual = monto_caja_actual + apuesta_f
                if (f2 == 1 and f1 == 1):
                    f1 = 0
                f2 = f2 - f1
                if ((f1 - f2) >= 0):
                    f1 = f1 - f2
                apuesta_f = f1 + f2
            else:
                monto_caja_actual = monto_caja_actual - apuesta_f
                f1 = f2
                f2 = apuesta_f
                apuesta_f = f1 + f2
            monto_caja.append(monto_caja_actual)


    if  (estrategia_elegida == "d"):
        # Elegimos el color ROJO para hacer la prueba
        apuesta_d = 10
        constante_suma_resta = 10
        for i in range(cant_tiradas):
            if(((monto_caja_actual - apuesta_d) < 0) and (tipo_capital == "f")):
                break
            if(valores[i] in numeros_rojos):
                monto_caja_actual = monto_caja_actual + apuesta_d
                if(apuesta_d > 10):
                    apuesta_d = apuesta_d - constante_suma_resta
            else:
                monto_caja_actual = monto_caja_actual - apuesta_d
                apuesta_d = apuesta_d + constante_suma_resta
            monto_caja.append(monto_caja_actual)


    montos_cajas_corrida.append(monto_caja)

    axs[0].plot(monto_caja, label=f"Frecuencia relativa de victorias en la corrida")
    axs[0].set_xlabel('Número de tiradas')
    axs[0].set_ylabel('Cantidad de capital')
    axs[0].set_title(f'Flujo de caja')

plt.savefig("Graficas.png")
plt.show()






