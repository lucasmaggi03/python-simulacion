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

print("")
if (tipo_test_aleatorio == "media_cuadrado"):
    for i in range(cant_valores_generados):
        valor_cuadrado = (semilla_generadora**2)
        valores_aleatorios_generados.append(valor_cuadrado)
        valor_cuadrado_binario = bin(valor_cuadrado)[2:]
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
        valores_aleatorios_generados_binarios.append(semilla_generadora_binaria)
        print(f'[{i}]    {semilla_generadora}     {semilla_generadora_binaria}')

if (tipo_test_aleatorio == "random_python"):
    for i in range(cant_valores_generados):
        valor_generado = random.randint(1, 2**32)
        valores_aleatorios_generados.append(valor_generado)
        valor_generado_binario = bin(valor_generado)[2:]
        valores_aleatorios_generados_binarios.append(valor_generado_binario)
        print(f'[{i}]       {valor_generado}     {valor_generado_binario}')




#Transformar valores_aleatorios_generados_binarios (contiene strings binarios) en bits individuales y despues contamos los ceros, unos y la cantidad de digitos
bits = [int(bit) for bin_str in valores_aleatorios_generados_binarios for bit in bin_str]
numeros_uno = bits.count(1)
numeros_cero = bits.count(0)
cantidad_digitos_binarios = len(bits)
print("")
print("Lista de bits")
print(bits)




## Prueba de autocorrelacion
n = len(bits)
matches = sum(bits[i] == bits[i + 1] for i in range(n - 1))
p = 0.5
expected = (n - 1) * p
variance = (n - 1) * p * (1 - p)
z = (matches - expected) / (variance ** 0.5)
print("")
print("PRUEBA DE AUTOCORRELACION")
print(f"Autocorrelación con desfase {1}: z = {z}")
if abs(z) < 1.96:
    print("Resultado: La secuencia pasa la prueba de autocorrelación (nivel de confianza 95%).")
else:
    print("Resultado: La secuencia NO pasa la prueba de autocorrelación.")




## Prueba de corridas o Runs Test
n = len(bits)
pr = sum(bits) / n  # proporción de unos

print("")
print("PRUEBA DE CORRIDAS O RUNS TEST")
# Chequeo previo: la proporción debe estar razonablemente cerca de 0.5
if abs(pr - 0.5) > 0.2:
    print(f"Proporción de unos (pi) = {pr}")
    print("La secuencia tiene un sesgo muy fuerte. No se puede aplicar el Runs Test.")
else:
    # Contar número de corridas (cambios entre 0s y 1s)
    Vn = 1 + sum(bits[i] != bits[i + 1] for i in range(n - 1))

    # Calcular valor esperado y varianza
    expected = 2 * n * pr * (1 - pr)
    variance = (2 * n * pr * (1 - pr) * (2 * n * pr * (1 - pr) - 1)) / (n - 1)
    z = (Vn - expected) / (variance ** 0.5)

    # Mostrar resultados
    print(f"Proporción de unos (pr): {pr}")
    print(f"Número de corridas observadas (Vn): {Vn}")
    print(f"Valor esperado de corridas: {expected}")
    print(f"Varianza: {variance}")
    print(f"Estadístico z: {z}")

    if abs(z) < 1.96:
        print("Resultado: La secuencia pasa el Runs Test (nivel de confianza 95%).")
    else:
        print("Resultado: La secuencia NO pasa el Runs Test.")




## Prueba Monobit y transformacion de los numeros generados a binario
print("")
print("PRUEBA DE MONOBIT")
print("Cantidad de ceros: ", numeros_cero)
print("Cantidad de unos: ", numeros_uno)
print("Cantidad de dig binarios: ", cantidad_digitos_binarios)
print("Porcentaje de unos: ", (numeros_uno/cantidad_digitos_binarios)*100)
print("Porcentaje de ceros: ", (numeros_cero/cantidad_digitos_binarios)*100)

numero_verificacion_monobit = abs(numeros_uno - numeros_cero) / math.sqrt(cantidad_digitos_binarios)
print("Numero de verificacion de test monobit: ", numero_verificacion_monobit)
if numero_verificacion_monobit < 1.96:
    print("La secuencia pasa la prueba Monobit (nivel de confianza 95%).")
else:
    print("La secuencia NO pasa la prueba Monobit.")





## Kolmogorov smirnov test
# Normalizamos los datos para que estén en el rango [0, 1] con criterio MIN-MAX
valores_aleatorios_generados_normalizados = [(x - min(valores_aleatorios_generados)) / (max(valores_aleatorios_generados) - min(valores_aleatorios_generados)) for x in valores_aleatorios_generados]
kstest_result = ss.kstest(valores_aleatorios_generados_normalizados, 'uniform')
print("")
print("PRUEBA DE KOLMOGOROV SMIRNOV")
print(f"Estadístico de la prueba (Kstest): {kstest_result.statistic}")
print(f"Valor p (Kstest): {kstest_result.pvalue}")
if(kstest_result.pvalue >= 0.05):
    print("Los numeros generados parecen seguir una distribucion uniforme")
else:
    print("Los numeros generados NO parecen seguir una distribucion uniforme")




## Grafica de dispersion
plt.figure(figsize=(10, 6))
plt.scatter(range(len(valores_aleatorios_generados)), valores_aleatorios_generados,s=0.5,color='black')
plt.title('Gráfica de Dispersión de Números Generados')
plt.xlabel('Índice')
plt.ylabel('Valor Generado')
plt.savefig('Grafica_dispersion.png') 
plt.show()





## Histograma de numeros generados
plt.figure(figsize=(10, 6))
plt.hist(valores_aleatorios_generados, bins=30, edgecolor='k', alpha=0.7)
plt.title('Histograma de los Números Generados')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.savefig('Histograma_numeros_generados.png') 
plt.show()




## Grafica de distribucion de ceros y unos binarios
plt.figure(figsize=(8,6))
plt.bar(["Ceros", "Unos"], [((numeros_cero/cantidad_digitos_binarios)*100), ((numeros_uno/cantidad_digitos_binarios)*100)], color='blue')
plt.xlabel('Valor')
plt.grid(True)
plt.ylabel('Distribucion binaria')
plt.title('Monobit test')
plt.savefig('Monobit_test.png')        
plt.show()



