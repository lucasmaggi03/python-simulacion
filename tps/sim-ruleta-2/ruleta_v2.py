import random 
import matplotlib.pyplot as plt
import numpy as np
import sys

tipo_capital = sys.argv[8]
estrategia_elegida = sys.argv[6]
num_corridas = int(sys.argv[2])
cant_tiradas = int(sys.argv[4])
valores_corrida = []
montos_cajas_corrida = []
indice_cant_intentos_corrida = []
frec_rel_cant_intentos_repetidos_corrida = []
cont_bancarrota = 0

if sys.argv[1] != '-c' or sys.argv[3] != '-n' or sys.argv[5] != '-s' or sys.argv[7] !='-a' :
    print("Uso: python ruleta_v2.py -c <corridas> -n <tiradas> -s <estrategia(m,f,d)> -a <capital(f,i)>")
    sys.exit(1)

numeros_rojos = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
numeros_columnas = [[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36]]
numeros_filas = [[1,4,7,10,13,16,19,22,25,28,31,34],[2,5,8,11,14,17,20,23,26,29,32,35],[3,6,9,12,15,18,21,24,27,30,33,36]]


plt.axhline(y=10000, color='red', linestyle='--', label="Monto de caja inicial")
for j in range(num_corridas):
    #Elegimos el monto caja inicial de 10000 U.M.
    monto_caja_actual = 10000
    valores = [random.randint(0,36) for i in range(cant_tiradas)]
    valores_corrida.append(valores)
    monto_caja = []
    tiradas_para_ganar = []
    frec_rel_cant_intentos_repetidos = []
    indice_cant_intentos = []
    cont_repeticiones = 1


    if (estrategia_elegida == "m"):
        apuesta_m = 10
        # Elegimos el color ROJO para hacer la prueba
        for i in range(cant_tiradas):
            if(((monto_caja_actual - apuesta_m) < 0) and (tipo_capital == "f")):
                cont_bancarrota = cont_bancarrota + 1
                break
            if(valores[i] in numeros_rojos):
                monto_caja_actual = monto_caja_actual + apuesta_m
                apuesta_m = 10
                tiradas_para_ganar.append(cont_repeticiones)
                cont_repeticiones = 1
            else:
                monto_caja_actual = monto_caja_actual - apuesta_m
                apuesta_m = apuesta_m*2
                cont_repeticiones = cont_repeticiones + 1
            monto_caja.append(monto_caja_actual)


    if  (estrategia_elegida == "f"):
        # Elegimos el color ROJO para hacer la prueba
        f1 = 0
        f2 = 1
        apuesta_f = f1 + f2
        for i in range(cant_tiradas):
            if(((monto_caja_actual - apuesta_f) < 0) and (tipo_capital == "f")):
                cont_bancarrota = cont_bancarrota + 1
                break
            if(valores[i] in numeros_rojos):
                monto_caja_actual = monto_caja_actual + apuesta_f
                if (f2 == 1 and f1 == 1):
                    f1 = 0
                f2 = f2 - f1
                if ((f1 - f2) >= 0):
                    f1 = f1 - f2
                apuesta_f = f1 + f2
                tiradas_para_ganar.append(cont_repeticiones)
                cont_repeticiones = 1
            else:
                monto_caja_actual = monto_caja_actual - apuesta_f
                f1 = f2
                f2 = apuesta_f
                apuesta_f = f1 + f2
                cont_repeticiones = cont_repeticiones + 1
            monto_caja.append(monto_caja_actual)


    if  (estrategia_elegida == "d"):
        # Elegimos el color ROJO para hacer la prueba
        apuesta_d = 10
        constante_suma_resta = 10
        for i in range(cant_tiradas):
            if(((monto_caja_actual - apuesta_d) < 0) and (tipo_capital == "f")):
                cont_bancarrota = cont_bancarrota + 1
                break
            if(valores[i] in numeros_rojos):
                monto_caja_actual = monto_caja_actual + apuesta_d
                if(apuesta_d > 10):
                    apuesta_d = apuesta_d - constante_suma_resta
                tiradas_para_ganar.append(cont_repeticiones)
                cont_repeticiones = 1
            else:
                monto_caja_actual = monto_caja_actual - apuesta_d
                apuesta_d = apuesta_d + constante_suma_resta
                cont_repeticiones = cont_repeticiones + 1
            monto_caja.append(monto_caja_actual)


    if  (estrategia_elegida == "x"):
        # Apostamos a las filas y columnas contrarias del numero que salio
        apuesta_x = 10
        for i in range(cant_tiradas):
            if(((monto_caja_actual - apuesta_x) < 0) and (tipo_capital == "f")):
                cont_bancarrota = cont_bancarrota + 1
                break
            if(i > 0):
                for j in range(3):
                    if valores[i-1] in numeros_columnas[j]:
                        columna_anterior = j
                    if valores[i-1] in numeros_filas[j]:
                        fila_anterior = j
                if((valores[i] not in numeros_columnas[columna_anterior]) and (valores[i] not in numeros_filas[fila_anterior])):
                    monto_caja_actual = monto_caja_actual + (apuesta_x * 2)
                    tiradas_para_ganar.append(cont_repeticiones)
                    cont_repeticiones = 1
                elif((valores[i] not in numeros_columnas[columna_anterior]) or (valores[i] not in numeros_filas[fila_anterior])):
                    monto_caja_actual = monto_caja_actual - apuesta_x
                    cont_repeticiones = cont_repeticiones + 1
                else:
                    monto_caja_actual = monto_caja_actual - (apuesta_x * 4)
                    cont_repeticiones = cont_repeticiones + 1
            monto_caja.append(monto_caja_actual)


    cant_intentos_repetidos = []
    for i in range(max(tiradas_para_ganar)):
        indice_cant_intentos.append(i+1)
        num = tiradas_para_ganar.count(i+1)
        cant_intentos_repetidos.append(num/cant_tiradas)
    sum_intentos_repetidos = sum(cant_intentos_repetidos)
    for i in range(max(tiradas_para_ganar)):
        frec_rel_cant_intentos_repetidos.append(cant_intentos_repetidos[i]/sum_intentos_repetidos)
    print(frec_rel_cant_intentos_repetidos)
    print(indice_cant_intentos)
    frec_rel_cant_intentos_repetidos_corrida.append(frec_rel_cant_intentos_repetidos)
    indice_cant_intentos_corrida.append(indice_cant_intentos)

    montos_cajas_corrida.append(monto_caja)

    plt.plot(monto_caja, label=f"Frecuencia relativa de victorias en la corrida")
    plt.xlabel('Número de tiradas')
    plt.ylabel('Cantidad de capital')
    plt.title(f'Flujo de caja, cantidad de veces en bancarrota: {cont_bancarrota}, cant de corridas: {num_corridas}')

plt.savefig("Graficas.png")
plt.show()

for i in range (num_corridas):
    plt.figure(figsize=(8,6))
    plt.bar(indice_cant_intentos_corrida[i], frec_rel_cant_intentos_repetidos_corrida[i], color='blue')
    plt.xlabel('Numero de Tiradas')
    plt.ylabel('Frecuencia Relativa')
    plt.title(f'Frecuencia relativa de obtener la apuesta favorable en corrida: {(i+1)}')
    plt.savefig(f'grafica_frecuencia_relativa_corrida{(i+1)}.png')        
    plt.show()






