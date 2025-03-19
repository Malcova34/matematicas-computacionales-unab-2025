import numpy as np
import math

def calcular_error_propagado(f, df, x_aprox, delta_x):
    """
    Calcula el error propagado en una función f evaluada en x_aprox,
    dado un error delta_x en x_aprox.
    
    Parámetros:
    f: función para evaluar
    df: derivada de la función f
    x_aprox: valor aproximado de x
    delta_x: error en x_aprox
    
    Retorna:
    El error propagado en f(x_aprox)
    """
    # Calcular el error propagado usando la fórmula ∆f(x̃) = f'(x̃) * ∆x̃
    error_propagado = abs(df(x_aprox) * delta_x)
    
    return error_propagado

# Problema 1: f(x) = 1.1x^4 - 1.9x^3 + 1.2x^2 - 2x + 4
def funcion1(x):
    return 1.1 * x**4 - 1.9 * x**3 + 1.2 * x**2 - 2 * x + 4

def derivada1(x):
    return 4.4 * x**3 - 5.7 * x**2 + 2.4 * x - 2

# Problema 2: f(x) = cos(x) * ln(2x)
def funcion2(x):
    return np.cos(x) * np.log(2 * x)

def derivada2(x):
    # Derivada usando la regla del producto
    # d/dx[cos(x) * ln(2x)] = -sin(x) * ln(2x) + cos(x) * (1/x)
    return -np.sin(x) * np.log(2 * x) + np.cos(x) * (1 / x)

# Valores para el problema 1
x_aprox1 = 1.4
delta_x1 = 0.05

# Valores para el problema 2
x_aprox2 = np.pi / 3
delta_x2 = 0.005

# Calcular el error propagado para el problema 1
error_propagado1 = calcular_error_propagado(funcion1, derivada1, x_aprox1, delta_x1)

# Calcular el error propagado para el problema 2
error_propagado2 = calcular_error_propagado(funcion2, derivada2, x_aprox2, delta_x2)

# Resultados
print("Problema 1:")
print(f"Valor aproximado x̃ = {x_aprox1}")
print(f"Error en x̃: ∆x̃ = {delta_x1}")
print(f"Función: f(x) = 1.1x^4 - 1.9x^3 + 1.2x^2 - 2x + 4")
print(f"Valor de f(x̃) = {funcion1(x_aprox1)}")
print(f"Valor de f'(x̃) = {derivada1(x_aprox1)}")
print(f"Error propagado: ∆f(x̃) = {error_propagado1}")
print()

print("Problema 2:")
print(f"Valor aproximado x̃ = {x_aprox2} (π/3)")
print(f"Error en x̃: ∆x̃ = {delta_x2}")
print(f"Función: f(x) = cos(x) * ln(2x)")
print(f"Valor de f(x̃) = {funcion2(x_aprox2)}")
print(f"Valor de f'(x̃) = {derivada2(x_aprox2)}")
print(f"Error propagado: ∆f(x̃) = {error_propagado2}")