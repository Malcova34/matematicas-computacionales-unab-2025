import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import math

# Datos proporcionados
x = np.array([0, 2, 4, 6, 8, 10, 12])
y = np.array([7.5, 1.8, -1, -1.8, -1.2, 2.2, 7.2])

# Preparar datos para regresión polinomial
x_reshaped = x.reshape(-1, 1)
poly_features = PolynomialFeatures(degree=2)
x_poly = poly_features.fit_transform(x_reshaped)

# Realizar la regresión
model = LinearRegression()
model.fit(x_poly, y)

# Obtener coeficientes
coef = model.coef_
intercept = model.intercept_

# Función polinómica ajustada (ax² + bx + c)
a = coef[2]
b = coef[1]
c = intercept

print(f"Coeficientes del polinomio ajustado: y = {a:.4f}x² + {b:.4f}x + {c:.4f}")

# Generar predicciones para visualización
x_continuo = np.linspace(min(x), max(x), 100)
x_continuo_reshaped = x_continuo.reshape(-1, 1)
x_continuo_poly = poly_features.transform(x_continuo_reshaped)
y_pred_continuo = model.predict(x_continuo_poly)

# Predicciones para los puntos originales
y_pred = model.predict(x_poly)

# Calcular coeficiente de determinación (R²)
r2 = r2_score(y, y_pred)
print(f"Coeficiente de determinación (R²): {r2:.4f}")

# Calcular coeficiente de correlación (r)
r = math.sqrt(abs(r2))  # Tomamos el valor absoluto para evitar problemas con números negativos
print(f"Coeficiente de correlación (r): {r:.4f}")

# Crear gráfica
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x_continuo, y_pred_continuo, color='red', label=f'Ajuste: {a:.4f}x² + {b:.4f}x + {c:.4f}')
plt.title('Ajuste de polinomio de segundo grado')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# Mostrar tabla de valores originales vs predichos
print("\nComparación de valores originales y predichos:")
print("   x   |   y   | y_pred |   Error  ")
print("-----------------------------")
for i in range(len(x)):
    error = y[i] - y_pred[i]
    print(f" {x[i]:5.1f} | {y[i]:5.1f} | {y_pred[i]:6.2f} | {error:8.2f}")