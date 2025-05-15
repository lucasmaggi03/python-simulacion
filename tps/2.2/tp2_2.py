import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss



# Generar numeros pseudoaleatorios con distribucion de probabilidad uniforme
num_uniformes = np.random.uniform(0,1,1000) #Genera 1000 valores pseudoaleatorios con distribucion uniforme entre 0 y 1
#Graficar valores uniformes
plt.figure(figsize=(8, 4))
plt.hist(num_uniformes, bins=50, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Datos simulados')
# Calculo de probabilidad teorica
valores_referencia_x = np.linspace(0, 1, 100) # Crea 100 numeros equiespaciados entre 0 y 1
valores_referencia_y = [1 / (1- 0)] * 100 # Calculado con la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'r--', linewidth=2, label='Probabilidad teórica')
plt.title('Distribucion uniforme')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Uniforme.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




# Generar numeros pseudoaleatorios con distribucion de probabilidad exponencial (Usando transformada inversa)
num_uniformes_para_exponencial = np.random.uniform(0,1,1000) # num_uniformes_para_exponencial ~ U(0,1)
num_exponenciales = -np.log(1 - num_uniformes_para_exponencial) / 1.5 # 1.5 es el valor de LAMBDA, λ = 1.5
# Graficar valores exponenciales
plt.figure(figsize=(8, 4))
plt.hist(num_exponenciales, bins=50, density=True, alpha=0.6, color='skyblue', label='Datos simulados')
# Calculo de probabilidad teorica
valores_referencia_x = np.linspace(0, np.max(num_exponenciales), 1000) # Crea 1000 numeros equiespaciados entre 0 y el maximo de la exponencial
valores_referencia_y = 1.5 * np.exp(-1.5 * valores_referencia_x) # 1.5 es el valor de LAMBDA, esto se calcula con la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'r-', label='Probabilidad teorica')
plt.title('Distribucion exponencial')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Exponencial.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



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
plt.title('Distribucion gamma')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Gamma.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


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
plt.title('Distribucion normal')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Normal.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



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
plt.title('Distribucion pascal')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Pascal.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Generar numeros con distribucion de probabilidad binomial
num_ensayos = 10   # número de ensayos
prob_exito = 0.4         # probabilidad de éxito
num_binomial = np.random.binomial(num_ensayos, prob_exito, size=1000) # Genera 1000 valores con distribucion de probabilidad binomial
# Representacion grafica de los datos
valores, veces_que_salen = np.unique(num_binomial, return_counts=True) # Esto es para trabajar con datos discretos (ya que la binomial al igual que la pascal trabajan con datos discretos), busca los valores unicos en el array num_pascal y cuenta cuantas veces aparece cada uno, guarda ambos.
prob_empirica = veces_que_salen / 1000  # Esto normaliza los conteos para convertirlos en una probabilidad empirica (lo divide por n muestras)
plt.figure(figsize=(8, 4))
plt.bar(valores, prob_empirica, width=0.8, alpha=0.6, label="Datos simulados", color='skyblue')
# Calculo de probabilidad teorica
valores_referencia_x = np.arange(0, num_ensayos + 1) # Genera los valores que tomo la variable en el grafico de barras en el eje X
valores_referencia_y = ss.binom.pmf(valores_referencia_x, num_ensayos, prob_exito) # Usanso SS calculamos los valores de Y usando la funcion de densidad de probabilidad
plt.plot(valores_referencia_x, valores_referencia_y, 'ro', label="Probabilidad teorica")
plt.title('Distribucion Binomial')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.savefig('Grafica_Binomial.png') 
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()