import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, expand
from sympy.utilities.lambdify import lambdify

# Datos del problema
x_datos = np.array([1, 3, 5, 7, 9])
y_datos = np.array([3, 0, -1, 2.5, 1])
punto_estimacion = 4.25

# Función para calcular el polinomio de Lagrange de grado n
def lagrange_interpolacion(x_datos, y_datos, grado):
    # Si el grado es mayor que la cantidad de puntos disponibles - 1, ajustamos
    n = min(grado, len(x_datos) - 1)
    
    # Tomamos los primeros n+1 puntos para la interpolación
    x = x_datos[:n+1]
    y = y_datos[:n+1]
    
    # Variable simbólica para el polinomio
    t = symbols('t')
    
    # Inicializamos el polinomio
    polinomio = 0
    
    # Construimos el polinomio de Lagrange
    for i in range(len(x)):
        # Término base para cada punto
        termino = y[i]
        
        # Construcción del polinomio básico de Lagrange
        for j in range(len(x)):
            if i != j:
                termino *= (t - x[j]) / (x[i] - x[j])
        
        # Añadimos el término al polinomio
        polinomio += termino
    
    # Simplificamos y expandimos el polinomio para obtener la forma estándar
    polinomio_simplificado = expand(simplify(polinomio))
    
    # Creamos una función a partir del polinomio para evaluación numérica
    polinomio_funcion = lambdify(t, polinomio_simplificado)
    
    return polinomio_simplificado, polinomio_funcion

# Calculamos los polinomios para los grados requeridos
polinomio_grado1, funcion_grado1 = lagrange_interpolacion(x_datos, y_datos, 1)
polinomio_grado2, funcion_grado2 = lagrange_interpolacion(x_datos, y_datos, 2)
polinomio_grado3, funcion_grado3 = lagrange_interpolacion(x_datos, y_datos, 3)

# Evaluamos f(4.25) usando los diferentes polinomios
estimacion_grado1 = funcion_grado1(punto_estimacion)
estimacion_grado2 = funcion_grado2(punto_estimacion)
estimacion_grado3 = funcion_grado3(punto_estimacion)

# Visualización de resultados
print(f"Polinomio de grado 1: {polinomio_grado1}")
print(f"Polinomio de grado 2: {polinomio_grado2}")
print(f"Estimación de f(4.25) usando polinomio de grado 1: {estimacion_grado1}")
print(f"Estimación de f(4.25) usando polinomio de grado 2: {estimacion_grado2}")
print(f"Estimación de f(4.25) usando polinomio de grado 3: {estimacion_grado3}")

# Visualización gráfica
plt.figure(figsize=(12, 8))

# Puntos originales
plt.scatter(x_datos, y_datos, color='red', label='Datos originales', s=70, zorder=5)

# Rango para visualización de los polinomios
x_rango = np.linspace(min(x_datos) - 0.5, max(x_datos) + 0.5, 1000)

# Graficar los polinomios
y_grado1 = [funcion_grado1(x) for x in x_rango]
y_grado2 = [funcion_grado2(x) for x in x_rango]
y_grado3 = [funcion_grado3(x) for x in x_rango]

plt.plot(x_rango, y_grado1, label=f'Grado 1: {polinomio_grado1}', linewidth=2)
plt.plot(x_rango, y_grado2, label=f'Grado 2: {polinomio_grado2}', linewidth=2)
plt.plot(x_rango, y_grado3, label=f'Grado 3', linewidth=2)

# Marcar el punto de estimación
plt.scatter([punto_estimacion], [estimacion_grado1], color='green', s=100, label=f'f(4.25) ≈ {estimacion_grado1:.4f} (grado 1)', zorder=5)
plt.scatter([punto_estimacion], [estimacion_grado2], color='blue', s=100, label=f'f(4.25) ≈ {estimacion_grado2:.4f} (grado 2)', zorder=5)
plt.scatter([punto_estimacion], [estimacion_grado3], color='purple', s=100, label=f'f(4.25) ≈ {estimacion_grado3:.4f} (grado 3)', zorder=5)

plt.axvline(x=punto_estimacion, color='gray', linestyle='--', alpha=0.5)

# Configuración de la gráfica
plt.title('Interpolación de Lagrange para distintos grados', fontsize=15)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()

plt.show()