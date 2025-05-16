import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

print("")
print("DISTRIBUCION UNIFORME")
#DISTRIBUCIONES CONTINUAS
# Generar numeros pseudoaleatorios con distribucion de probabilidad uniforme
valor_inicial = 0
valor_final = 1
num_uniformes = np.random.uniform(valor_inicial,valor_final,1000) #Genera 1000 valores pseudoaleatorios con distribucion uniforme entre 0 y 1
#Graficar valores uniformes
plt.figure(figsize=(8, 4))
plt.hist(num_uniformes, bins=50, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Datos simulados')
# Calculo de probabilidad teorica
valores_referencia_x = np.linspace(0, 1, 100) # Crea 100 numeros equiespaciados entre 0 y 1
valores_referencia_y = [valor_final / (valor_final - valor_inicial)] * 100 # Calculado con la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'r--', linewidth=2, label='Probabilidad teórica')
plt.title(f'Distribución Uniforme continua\n[a={0}, b={1}]')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Uniforme.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion uniforme simulada es: ", np.mean(num_uniformes))
#Kolmogorov-Smirnov
estadistico, valor_p = ss.kstest(num_uniformes, 'uniform', args=(valor_inicial, valor_final - valor_inicial))
print("Uniforme - D:", estadistico, "| p-valor:", valor_p)
if(valor_p > 0.05):
    print("El valor de P es mayor a 0.05 por lo tanto podemos afirmar que los datos generados parecen seguir una distribucion uniforme")
else:
    print("El valor de P es menor a 0.05 por lo tanto podemos decir que los datos generados NO parecen seguir una distribucion uniforme")



print("")
print("DISTRIBUCION EXPONENCIAL")
# Generar numeros pseudoaleatorios con distribucion de probabilidad exponencial (Usando transformada inversa)
lambd = 1.5 # Valor de LAMBDA
num_uniformes_para_exponencial = np.random.uniform(0,1,1000) # num_uniformes_para_exponencial ~ U(0,1)
num_exponenciales = -np.log(1 - num_uniformes_para_exponencial) / lambd # 1.5 es el valor de LAMBDA, λ = 1.5
# Graficar valores exponenciales
plt.figure(figsize=(8, 4))
plt.hist(num_exponenciales, bins=50, density=True, alpha=0.6, color='skyblue', label='Datos simulados')
# Calculo de probabilidad teorica
valores_referencia_x = np.linspace(0, np.max(num_exponenciales), 1000) # Crea 1000 numeros equiespaciados entre 0 y el maximo de la exponencial
valores_referencia_y = lambd * np.exp(-lambd * valores_referencia_x) # 1.5 es el valor de LAMBDA, esto se calcula con la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'r-', label='Probabilidad teorica')
plt.title('Distribución Exponencial (λ = {})'.format(lambd))
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Exponencial.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion exponencial simulada es: ", np.mean(num_exponenciales))
#Kolmogorov-Smirnov
estadistico, valor_p = ss.kstest(num_exponenciales, 'expon', args=(0, 1 / lambd))
print("Exponencial - D:", estadistico, "| p-valor:", valor_p)
if(valor_p > 0.05):
    print("El valor de P es mayor a 0.05 por lo tanto podemos afirmar que los datos generados parecen seguir una distribucion exponencial")
else:
    print("El valor de P es menor a 0.05 por lo tanto podemos decir que los datos generados NO parecen seguir una distribucion exponencial")


print("")
print("DISTRIBUCION GAMMA")
# Generar numeros pseudoaleatorios con distribucion de probabilidad gamma
alpha = 2.0   # forma (k)
beta = 1.0    # escala
num_gamma = np.random.gamma(alpha, beta, 1000) # Genera 1000 valores con distribuccion GAMMA
# Representacion grafica de los datos
plt.figure(figsize=(8, 4))
plt.hist(num_gamma, bins=50, density=True, alpha=0.6, color='skyblue', label='Datos simulados')
# Calculo de probabilidad teorica
valores_referencia_x = np.linspace(0, np.max(num_gamma), 1000) # Crea 1000 numeros equiespaciados entre 0 y el maximo de los valors con distrubuccion gamma generados
valores_referencia_y = ss.gamma.pdf(valores_referencia_x, a=alpha, scale=beta) # Usamos una funcion de la libreria scipy.stats para calcular los valores de y con la funcion de de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y , 'r-', label='Probabilidad teorica')
plt.title(f'Distribución Gamma (α = {alpha}, β = {beta})')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Gamma.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion gamma es: ", np.mean(num_gamma))
print("La varianza de la distribucion gamma es: ", np.var(num_gamma))
#Kolmogorov-Smirnov
estadistico, valor_p = ss.kstest(num_gamma, 'gamma', args=(alpha, 0, beta))
print("Gamma - D:", estadistico, "| p-valor:", valor_p)
if(valor_p > 0.05):
    print("El valor de P es mayor a 0.05 por lo tanto podemos afirmar que los datos generados parecen seguir una distribucion gamma")
else:
    print("El valor de P es menor a 0.05 por lo tanto podemos decir que los datos generados NO parecen seguir una distribucion gamma")


print("")
print("DISTRIBUCION NORMAL")
# Generar numeros pseudoaleatorios con distribucion de probabilidad normal
mu = 0      # media
sigma = 1   # desviación estándar
num_normal = np.random.normal(mu, sigma, 1000) # Genera 1000 numeros con distribucion de probabilidad normal
# Representacion grafica de los numeros generados
plt.figure(figsize=(8, 4))
plt.hist(num_normal, bins=50, density=True, alpha=0.6, color='skyblue', label='Datos simulados')
# Calculo de probabilidad teorica
valores_referencia_x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)  # esto genera 1000 puntos equiespaciados entre mu - 4sigma y mu + 4sigma ya que la mayor parte de la masa de una distribucion normal esta contenida dentro de ese intervalo
valores_referencia_y = ss.norm.pdf(valores_referencia_x, loc=mu, scale=sigma) # Calculamos los valores de Y usando la libreria scipy stats, esta usa la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'r-', label='Probabilidad Teorica')
plt.title(f'Distribución Normal (μ = {mu}, σ = {sigma})')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Normal.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion normal es: ", np.mean(num_normal))
print("La desviacion estandar de la distribucion normal es: ", np.std(num_normal))
#Kolmogorov-Smirnov
estadistico, valor_p = ss.kstest(num_normal, 'norm', args=(mu, sigma))
print("Normal - D:", estadistico, "| p-valor:", valor_p)
if(valor_p > 0.05):
    print("El valor de P es mayor a 0.05 por lo tanto podemos afirmar que los datos generados parecen seguir una distribucion normal")
else:
    print("El valor de P es menor a 0.05 por lo tanto podemos decir que los datos generados NO parecen seguir una distribucion normal")



# DISTRIBUCIONES DISCRETAS
print("")
print("DISTRIBUCION PASCAL")
# Generar numeros con distribucion de probabilidad pascal (binomial negativa)
exitos_deseados = 5       # número de éxitos deseados
probabilidad_exito = 0.3     # probabilidad de éxito
num_pascal = np.random.negative_binomial(exitos_deseados, probabilidad_exito, 1000) # Genera 1000 valores con distribucion binomial negativa o pascal
valores, veces_que_salen = np.unique(num_pascal, return_counts=True) # Esto es para trabajar con datos discretos (ya que pascal trabaja con datos discretos), busca los valores unicos en el array num_pascal y cuenta cuantas veces aparece cada uno, guarda ambos.
prob_empirica = veces_que_salen / 1000 # Esto normaliza los conteos para convertirlos en una probabilidad empirica (lo divide por n muestras)
# Grafico de resultados
plt.figure(figsize=(8, 4))
plt.bar(valores, prob_empirica, width=0.8, alpha=0.6, label="Datos simulados", color='skyblue')
# Calculo de probabilidad teorica
valores_referencia_x = np.arange(0, max(num_pascal)+1) # Genera los valores que tomo la variable en el grafico de barras en el eje X
valores_referencia_y = ss.nbinom.pmf(valores_referencia_x, exitos_deseados, probabilidad_exito) # Usanso SS calculamos los valores de Y usando la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'ro', label="Probabilidad Teorica")
plt.title(f'Distribución Pascal (r = {exitos_deseados}, p = {probabilidad_exito})')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Pascal.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion pascal es: ", np.mean(num_pascal))
print("La varianza de la distribucion pascal es: ", np.var(num_pascal))
media_teorica = exitos_deseados * (1 - probabilidad_exito) / probabilidad_exito
var_teorica = exitos_deseados * (1 - probabilidad_exito) / (probabilidad_exito ** 2)
print("La media teorica de la distribucion pascal es: ", media_teorica)
print("La varianza teorica de la distribucion pascal es: ", var_teorica)


print("")
print("DISTRIBUCION BINOMIAL")
# Generar numeros con distribucion de probabilidad binomial
num_ensayos = 10   # número de ensayos
prob_exito = 0.4         # probabilidad de éxito
num_binomial = np.random.binomial(num_ensayos, prob_exito, size=1000) # Genera 1000 valores con distribucion de probabilidad binomial
# Representacion grafica de los datos
valores, veces_que_salen = np.unique(num_binomial, return_counts=True) # Esto es para trabajar con datos discretos (ya que la binomial al igual que la pascal trabajan con datos discretos), busca los valores unicos en el array num_binomial y cuenta cuantas veces aparece cada uno, guarda ambos.
prob_empirica = veces_que_salen / 1000  # Esto normaliza los conteos para convertirlos en una probabilidad empirica (lo divide por n muestras)
plt.figure(figsize=(8, 4))
plt.bar(valores, prob_empirica, width=0.8, alpha=0.6, label="Datos simulados", color='skyblue')
# Calculo de probabilidad teorica
valores_referencia_x = np.arange(0, num_ensayos + 1) # Genera los valores que tomo la variable en el grafico de barras en el eje X
valores_referencia_y = ss.binom.pmf(valores_referencia_x, num_ensayos, prob_exito) # Usando SS calculamos los valores de Y usando la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'ro', label="Probabilidad teorica")
plt.title(f'Distribución Binomial (n = {num_ensayos}, p = {prob_exito})')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Binomial.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion pascal es: ", np.mean(num_binomial))
print("La varianza de la distribucion pascal es: ", np.var(num_binomial))
media_teorica = num_ensayos * prob_exito
var_teorica = num_ensayos * prob_exito * (1 - prob_exito)
print("La media teorica de la distribucion BINOMIAL es: ", media_teorica)
print("La varianza teorica de la distribucion BINOMIAL es: ", var_teorica)



print("")
print("DISTRIBUCION HIPERGEOMETRICA")
# Generar numeros con distribucion de probabilidad hipergeometrica
tam_total = 50      # tamaño total de la población
num_exitos = 15      # número de éxitos en la población
num_extracciones = 10      # número de extracciones
num_hipergeometrico = np.random.hypergeometric(ngood=num_exitos, nbad=tam_total-num_exitos, nsample=num_extracciones, size=1000) # Genera 1000 valores con distribucion de probabilidad hipergeometrica
# Representacion grafica
valores, veces_que_salen = np.unique(num_hipergeometrico, return_counts=True) # Esto es para trabajar con datos discretos (ya que la hipergeometrica es discreta), busca los valores unicos en el array num_hipergeometrico y cuenta cuantas veces aparece cada uno, guarda ambos.
prob_empirica = veces_que_salen / 1000 # Esto normaliza los conteos para convertirlos en una probabilidad empirica (lo divide por n muestras)
plt.figure(figsize=(8, 4))
plt.bar(valores, prob_empirica, width=0.8, alpha=0.6, label="Datos simulados", color='skyblue')
# Calculo de probabilidad teorica
valores_referencia_x = np.arange(0, num_extracciones+1) # Genera los valores que tomo la variable en el grafico de barras en el eje X
valores_referencia_y = ss.hypergeom.pmf(valores_referencia_x, tam_total, num_exitos, num_extracciones) #Usando SS calculamos los valores de Y usando la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'ro', label='Probabilidad Teorica')
plt.title(f'Distribución Hipergeométrica (N={tam_total}, K={num_exitos}, n={num_extracciones})')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Hipergeometrica.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion hipergeometrica es: ", np.mean(num_hipergeometrico))
print("La varianza de la distribucion hipergeometrica es: ", np.var(num_hipergeometrico))
media_teorica = num_extracciones * (num_exitos / tam_total)
var_teorica = num_extracciones * (num_exitos / tam_total) * ((tam_total - num_exitos) / tam_total) * ((tam_total - num_extracciones) / (tam_total - 1))
print("La media teorica de la distribucion Hipergeometrica es: ", media_teorica)
print("La varianza teorica de la distribucion Hipergeometrica es: ", var_teorica)


print("")
print("DISTRIBUCION POISSON")
# Generar numeros con distribucion de probabilidad Poisson
lambd = 4 # Tasa de eventos, valor de LAMBDA
num_poisson = np.random.poisson(lam=lambd, size=1000) # Genera 1000 valores con distribucion de poisson
# Representacion grafica
valores, veces_que_salen = np.unique(num_poisson, return_counts=True) # Esto es para trabajar con datos discretos (ya que la Poisson es discreta), busca los valores unicos en el array num_poisson y cuenta cuantas veces aparece cada uno, guarda ambos.
prob_empirica = veces_que_salen / 1000
plt.figure(figsize=(8, 4))
plt.bar(valores, prob_empirica, width=0.8, alpha=0.6, label='Datos simulados', color='skyblue')
# Calculo de probabilidad teorica
valores_referencia_x = np.arange(0, max(num_poisson)+1) # Genera los valores que tomo la variable en el grafico de barras en el eje X
valores_referencia_y = ss.poisson.pmf(valores_referencia_x, mu=lambd) #Usando SS calculamos los valores de Y usando la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'ro', label='PMF teórica')
plt.title(f'Distribución de Poisson (λ={lambd})')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Poisson.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion poisson es: ", np.mean(num_hipergeometrico))
print("La varianza de la distribucion poisson es: ", np.var(num_hipergeometrico))
# Teóricas (ambas iguales a λ en Poisson)
print("La media teorica de la distribucion poisson es: ", lambd)
print("La varianza teorica de la distribucion poisson es: ", lambd)



print("")
print("DISTRIBUCION EMPIRICA DISCRETA")
# Generar numeros con distribucion de probabilidad empirica discreta
# Primero vamos a generar 15 valores de forma aleatoria entre 0 y 10 ya que la distribucion empirica discreta se contruye a partir de un conjunto de datos objservados
datos_observados = np.random.uniform(0,10,15)
# Obtener valores y frecuencias de los datos observados
valores, veces_que_salen = np.unique(datos_observados, return_counts=True)
probabilidades = veces_que_salen / sum(veces_que_salen)
# Simular nuevos valores empiricos
num_empiricos = np.random.choice(valores, size=1000, p=probabilidades)
# Representacion grafica
valores_sim, veces_que_salen_sim = np.unique(num_empiricos, return_counts=True)
prob_empirica = veces_que_salen_sim / 1000
plt.figure(figsize=(8, 4))
plt.bar(valores_sim, prob_empirica, width=0.8, alpha=0.6, label='Datos simulados', color='skyblue')
# Valores teoricos
plt.figure(figsize=(8, 4))
plt.bar(valores_sim, prob_empirica, width=0.8, alpha=0.7, color='orange', label='Simulada')
plt.plot(valores, probabilidades, 'ro', label='Original (observada)')
plt.title('Distribución Empírica Discreta')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Empirica_Discreta.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
print("La media de la distribucion empirica discreta observada es: ", np.mean(datos_observados))
print("La media de la distribucion empirica discreta simulada es: ", np.mean(num_empiricos))
print("La varianza de la distribucion empirica discreta observada es: ", np.var(datos_observados))
print("La varianza de la distribucion empirica discreta simulada es: ", np.var(num_empiricos))