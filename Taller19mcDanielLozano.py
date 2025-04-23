import numpy as np
import matplotlib.pyplot as plt

# Datos del Taller 19
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1.5, 2.5, 3.5, 4.5, 6.5, 9.0])

# Transformación logarítmica
ln_y = np.log(y)

# Regresión lineal sobre ln(y)
n = len(x)
sum_x = np.sum(x)
sum_ln_y = np.sum(ln_y)
sum_x_ln_y = np.sum(x * ln_y)
sum_x2 = np.sum(x**2)

# Cálculo de beta y alpha
beta = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_x2 - sum_x**2)
ln_alpha = (sum_ln_y - beta * sum_x) / n
alpha = np.exp(ln_alpha)

# Mostrar el modelo
print("Modelo exponencial ajustado:")
print(f"y = {alpha:.3f} * e^({beta:.3f} * x)")

# Generar valores para la curva ajustada
x_model = np.linspace(min(x), max(x), 100)
y_model = alpha * np.exp(beta * x_model)

# Graficar puntos originales y modelo ajustado
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x_model, y_model, color='red', label='Modelo ajustado')
plt.title('Regresión Exponencial - Taller 19')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
