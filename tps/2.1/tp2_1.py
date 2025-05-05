import random 
import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import scipy.stats as ss

tipo_test_aleatorio = sys.argv[2]
semilla_generadora = int(sys.argv[4])
cant_valores_generados = int(sys.argv[6])

if sys.argv[1] != '-c' or sys.argv[3] != '-n' or sys.argv[5] !='-s':
    print("Uso: python tp2_1.py -c <media_cuadrado|gcl|random_python> -n <semilla_generadora> -s <cant_valores_generados>")
    sys.exit(1)

valores_aleatorios_generados = []
valores_aleatorios_generados_binarios = []
numeros_uno = 0
numeros_cero = 0

if (tipo_test_aleatorio == "media_cuadrado"):
    for i in range(cant_valores_generados):
        valor_cuadrado = (semilla_generadora**2)
        valores_aleatorios_generados.append(valor_cuadrado)
        valor_cuadrado_binario = bin(valor_cuadrado)[2:]
        numeros_uno = numeros_uno + valor_cuadrado_binario.count('1')
        numeros_cero = numeros_cero + valor_cuadrado_binario.count('0')
        valores_aleatorios_generados_binarios.append(valor_cuadrado_binario)
        valor_cuadrado_rellenado = str(valor_cuadrado).zfill(8)
        semilla_generadora = int(valor_cuadrado_rellenado[2:6])
        print(f'    [{i}]    {semilla_generadora}       {valor_cuadrado}      {valor_cuadrado_binario}')

if (tipo_test_aleatorio == "gcl"):
    for i in range(cant_valores_generados):
        a = 1664525
        c = 1013904223
        m = 2**32
        semilla_generadora = (a * semilla_generadora + c) % m
        valores_aleatorios_generados.append(semilla_generadora)
        semilla_generadora_binaria = bin(semilla_generadora)[2:]
        numeros_uno = numeros_uno + semilla_generadora_binaria.count('1')
        numeros_cero = numeros_cero + semilla_generadora_binaria.count('0')
        valores_aleatorios_generados_binarios.append(semilla_generadora_binaria)
        print(f'[{i}]    {semilla_generadora}     {semilla_generadora_binaria}')

if (tipo_test_aleatorio == "random_python"):
    for i in range(cant_valores_generados):
        valor_generado = random.randint(1, 2**32)
        valores_aleatorios_generados.append(valor_generado)
        valor_generado_binario = bin(valor_generado)[2:]
        numeros_uno = numeros_uno + valor_generado_binario.count('1')
        numeros_cero = numeros_cero + valor_generado_binario.count('0')
        valores_aleatorios_generados_binarios.append(valor_generado_binario)
        print(f'[{i}]       {valor_generado}     {valor_generado_binario}')


suma_ceros_unos = numeros_cero + numeros_uno
print("Cantidad de ceros: ", valores_aleatorios_generados_binarios.count('0'))
print("Cantidad de unos: ", valores_aleatorios_generados_binarios.count('1'))
print("Porcentaje de unos: ", (numeros_uno/suma_ceros_unos)*100)
print("Porcentaje de ceros: ", (numeros_cero/suma_ceros_unos)*100)


numero_verificacion_monobit = ((abs(numeros_uno - numeros_cero))/(math.sqrt(suma_ceros_unos)))
print("Numero de verificacion de test monobit: ", numero_verificacion_monobit)

kstest_result = ss.kstest(valores_aleatorios_generados, 'uniform', args=(min(valores_aleatorios_generados), max(valores_aleatorios_generados)-min(valores_aleatorios_generados)))
print(f"Estadístico de la prueba: {kstest_result.statistic}")
print(f"Valor p: {kstest_result.pvalue}")

plt.figure(figsize=(10, 6))
plt.scatter(range(len(valores_aleatorios_generados)), valores_aleatorios_generados,s=0.5,color='black')
plt.title('Gráfica de Dispersión de Números Generados')
plt.xlabel('Índice')
plt.ylabel('Valor Generado')
plt.savefig('Grafica_dispersion.png') 
plt.show()


plt.figure(figsize=(10, 6))
plt.hist(valores_aleatorios_generados, bins=30, edgecolor='k', alpha=0.7)
plt.title('Histograma de los Números Generados')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.savefig('Histograma_numeros_generados.png') 
plt.show()


plt.figure(figsize=(8,6))
plt.bar(["Ceros", "Unos"], [((numeros_cero/suma_ceros_unos)*100), ((numeros_uno/suma_ceros_unos)*100)], color='blue')
plt.xlabel('Valor')
plt.ylabel('Distribucion binaria')
plt.title('Monobit test')
plt.savefig('Monobit_test.png')        
plt.show()



