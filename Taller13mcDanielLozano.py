import numpy as np
import math

def factorial(n):
    """Calcula el factorial de un número."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def taylor_approximation(x, x0, order):
    
    # Valor real de f(x0) = e^(-x0)
    f_x0 = math.exp(-x0)
    
    # Primera derivada de f(x) = -e^(-x)
    # Segunda derivada de f(x) = e^(-x)
    # Tercera derivada de f(x) = -e^(-x)
    # ...
    # La n-ésima derivada de f(x) = (-1)^n * e^(-x)
    
    approximation = 0
    h = x - x0
    
    for n in range(order + 1):
        # La n-ésima derivada evaluada en x0: (-1)^n * e^(-x0)
        derivative_at_x0 = ((-1) ** n) * f_x0
        
        # Término de la serie de Taylor: f^(n)(x0) * (x-x0)^n / n!
        term = derivative_at_x0 * (h ** n) / factorial(n)
        
        approximation += term
        
    return approximation

def calculate_error(approximate, exact):
    """
    Calcula el error relativo porcentual.
    
    Parámetros:
    approximate -- valor aproximado
    exact -- valor exacto
    
    Retorna:
    Error relativo porcentual
    """
    return abs((exact - approximate) / exact) * 100

# Valores para el problema
x = 0.805
x0 = 0.8
exact_value = math.exp(-x)  # Valor exacto de e^(-0.805)

print(f"Valor exacto de e^(-{x}) = {exact_value}")
print("\nAproximaciones por serie de Taylor con base en x0 = {x0}:")
print("Orden\tAproximación\t\tError Relativo (%)")
print("-" * 60)

for order in range(16):  # Desde orden 0 hasta orden 15
    approximation = taylor_approximation(x, x0, order)
    error = calculate_error(approximation, exact_value)
    
    print(f"{order}\t{approximation:.10f}\t{error:.10f}")