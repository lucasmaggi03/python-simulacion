import random 
import matplotlib.pyplot as plt

random_values = [random.random() for _ in range(100)]
constant_values = [0.5 if i % 2 == 0 else 0.7 for i in range(100)]
plt.figure(figsize=(10,6))
plt.plot(random_values, label="Valores Aleatorios", color="blue")
plt.plot(constant_values, label="Valor Constante", linestyle="--", color="red")
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.title("Grafico de Valores Aleatorios con Valor Constante Intermitente")
plt.legend()
plt.grid(True)
plt.show()
