import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Datos del taller
x1 = np.array([1, 1, 2, 3, -1.5, 2, 3, 3])
x2 = np.array([0, 0.5, 0.5, 1, -1.2, 1.5, 1.5, 0.5])
y = np.array([0.2, 3, -0.8, -0.4, 3.5, 3.6, 0.5, -1])

# Crear la matriz de diseño con columna de 1s para el término independiente
X = np.column_stack((np.ones_like(x1), x1, x2))

# Calcular los coeficientes (a0, a1, a2) usando la fórmula normal: a = (X^T X)^(-1) X^T y
coefficients = np.linalg.inv(X.T @ X) @ X.T @ y
a0, a1, a2 = coefficients
print(f"Modelo: y = {a0:.4f} + {a1:.4f}*x1 + {a2:.4f}*x2")

# Predicción con el modelo
y_pred = X @ coefficients

# Coeficiente de determinación R²
Sr = np.sum((y - y_pred)**2)
St = np.sum((y - np.mean(y))**2)
R2 = 1 - Sr / St
r = np.sqrt(R2) if a1 != 0 or a2 != 0 else 0  # signo positivo por simplicidad

print(f"Coeficiente de determinación (R²): {R2:.4f}")
print(f"Coeficiente de correlación (r): {r:.4f}")

# Gráfica en 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Puntos reales
ax.scatter(x1, x2, y, color='red', label='Datos originales')

# Plano ajustado
x1_grid, x2_grid = np.meshgrid(np.linspace(min(x1), max(x1), 10),
                               np.linspace(min(x2), max(x2), 10))
y_grid = a0 + a1 * x1_grid + a2 * x2_grid
ax.plot_surface(x1_grid, x2_grid, y_grid, alpha=0.5, cmap='viridis', label='Plano de regresión')

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('Regresión Lineal Múltiple - Taller 22')
plt.legend()
plt.show()
