import math
import numpy as np
import matplotlib.pyplot as plt

def taylor_aproximacion(f, df, d2f, d3f, x0, x_objetivo):
    """
    Calcula aproximaciones de Taylor de orden 0 a 3 para f(x_objetivo)
    basado en los valores de f y sus derivadas en x0.
    
    Parámetros:
    f, df, d2f, d3f: Valores de la función y sus derivadas en x0
    x0: Punto base
    x_objetivo: Punto donde se desea aproximar la función
    
    Retorna:
    Lista con las aproximaciones de orden 0 a 3
    """
    h = x_objetivo - x0
    
    # Orden 0: f(x) ≈ f(x0)
    orden_0 = f
    
    # Orden 1: f(x) ≈ f(x0) + f'(x0)·h
    orden_1 = f + df * h
    
    # Orden 2: f(x) ≈ f(x0) + f'(x0)·h + f''(x0)·h²/2
    orden_2 = f + df * h + (d2f / 2) * (h**2)
    
    # Orden 3: f(x) ≈ f(x0) + f'(x0)·h + f''(x0)·h²/2 + f'''(x0)·h³/6
    orden_3 = f + df * h + (d2f / 2) * (h**2) + (d3f / 6) * (h**3)
    
    return [orden_0, orden_1, orden_2, orden_3]

def calcular_valor_real(funcion, x):
    """Calcula el valor real de la función en x"""
    return funcion(x)

def mostrar_resultados(aproximaciones, valor_real, orden_max=3):
    """Muestra los resultados de las aproximaciones y el error"""
    print("\nResultados de las aproximaciones:")
    for i in range(orden_max + 1):
        error = abs(aproximaciones[i] - valor_real)
        error_porcentual = (error / abs(valor_real)) * 100 if valor_real != 0 else float('inf')
        print(f"Orden {i}: {aproximaciones[i]:.8f} (Error: {error:.8f}, Error %: {error_porcentual:.4f}%)")

def graficar_aproximaciones(funcion, x0, x_objetivo, aproximaciones, titulo):
    """Grafica la función real y sus aproximaciones"""
    # Rango para la gráfica
    if x0 < x_objetivo:
        x_min, x_max = x0 - 0.1, x_objetivo + 0.1
    else:
        x_min, x_max = x_objetivo - 0.1, x0 + 0.1
    
    x = np.linspace(x_min, x_max, 1000)
    y_real = [funcion(xi) for xi in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_real, 'k-', label='Función real')
    
    # Crear funciones de aproximación
    def aprox_orden_0(x):
        return aproximaciones[0]
    
    def aprox_orden_1(x):
        h = x - x0
        return aproximaciones[0] + (aproximaciones[1] - aproximaciones[0]) / (x_objetivo - x0) * h
    
    def aprox_orden_2(x):
        h = x - x0
        df = (aproximaciones[1] - aproximaciones[0]) / (x_objetivo - x0)
        d2f = 2 * ((aproximaciones[2] - aproximaciones[0]) / (x_objetivo - x0)**2 - df / (x_objetivo - x0))
        return aproximaciones[0] + df * h + (d2f / 2) * (h**2)
    
    def aprox_orden_3(x):
        h = x - x0
        return aproximaciones[3]  # Simplificado para este ejemplo
    
    # Graficar aproximaciones
    y_aprox_0 = [aprox_orden_0(xi) for xi in x]
    plt.plot(x, y_aprox_0, 'r--', label='Orden 0')
    
    y_aprox_1 = [aprox_orden_1(xi) for xi in x]
    plt.plot(x, y_aprox_1, 'g--', label='Orden 1')
    
    y_aprox_2 = [aprox_orden_2(xi) for xi in x]
    plt.plot(x, y_aprox_2, 'b--', label='Orden 2')
    
    # Marcar puntos clave
    plt.plot(x0, funcion(x0), 'ko', label=f'Punto base x0={x0}')
    plt.plot(x_objetivo, funcion(x_objetivo), 'ro', label=f'Punto objetivo x={x_objetivo}')
    
    plt.title(titulo)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# ------------------------
# Primer ejercicio
# ------------------------
print("=== Primer ejercicio ===")
print("Función: f(x) = 0.3x³ - 1.8x² + 2.5x - 1")

# Definir la función y sus derivadas
def f1(x):
    return 0.3 * x**3 - 1.8 * x**2 + 2.5 * x - 1

def df1(x):
    return 0.9 * x**2 - 3.6 * x + 2.5

def d2f1(x):
    return 1.8 * x - 3.6

def d3f1(x):
    return 1.8  # Constante

# Punto base y objetivo
x0_1 = 0.4
x_objetivo_1 = 0.5

# Calcular valores en el punto base
f_x0_1 = f1(x0_1)
df_x0_1 = df1(x0_1)
d2f_x0_1 = d2f1(x0_1)
d3f_x0_1 = d3f1(x0_1)

print(f"Punto base: x0 = {x0_1}")
print(f"Punto objetivo: x = {x_objetivo_1}")
print(f"f({x0_1}) = {f_x0_1:.8f}")
print(f"f'({x0_1}) = {df_x0_1:.8f}")
print(f"f''({x0_1}) = {d2f_x0_1:.8f}")
print(f"f'''({x0_1}) = {d3f_x0_1:.8f}")

# Calcular aproximaciones
aproximaciones_1 = taylor_aproximacion(f_x0_1, df_x0_1, d2f_x0_1, d3f_x0_1, x0_1, x_objetivo_1)

# Calcular valor real
valor_real_1 = f1(x_objetivo_1)
print(f"Valor real f({x_objetivo_1}) = {valor_real_1:.8f}")

# Mostrar resultados
mostrar_resultados(aproximaciones_1, valor_real_1)

# ------------------------
# Segundo ejercicio
# ------------------------
print("\n=== Segundo ejercicio ===")
print("Función: f(x) = 1.4e^x - 3.2x + 2.4")

# Definir la función y sus derivadas
def f2(x):
    return 1.4 * math.exp(x) - 3.2 * x + 2.4

def df2(x):
    return 1.4 * math.exp(x) - 3.2

def d2f2(x):
    return 1.4 * math.exp(x)

def d3f2(x):
    return 1.4 * math.exp(x)

# Punto base y objetivo
x0_2 = 0.6
x_objetivo_2 = 0.65

# Calcular valores en el punto base
f_x0_2 = f2(x0_2)
df_x0_2 = df2(x0_2)
d2f_x0_2 = d2f2(x0_2)
d3f_x0_2 = d3f2(x0_2)

print(f"Punto base: x0 = {x0_2}")
print(f"Punto objetivo: x = {x_objetivo_2}")
print(f"e^{x0_2} ≈ {math.exp(x0_2):.8f}")
print(f"f({x0_2}) = {f_x0_2:.8f}")
print(f"f'({x0_2}) = {df_x0_2:.8f}")
print(f"f''({x0_2}) = {d2f_x0_2:.8f}")
print(f"f'''({x0_2}) = {d3f_x0_2:.8f}")

# Calcular aproximaciones
aproximaciones_2 = taylor_aproximacion(f_x0_2, df_x0_2, d2f_x0_2, d3f_x0_2, x0_2, x_objetivo_2)

# Calcular valor real
valor_real_2 = f2(x_objetivo_2)
print(f"Valor real f({x_objetivo_2}) = {valor_real_2:.8f}")

# Mostrar resultados
mostrar_resultados(aproximaciones_2, valor_real_2)

# ------------------------
# Resumen de resultados
# ------------------------
print("\n=== Resumen de resultados ===")
print(f"1. f(0.5) ≈ {aproximaciones_1[3]:.8f} (Valor real: {valor_real_1:.8f})")
print(f"2. f(0.65) ≈ {aproximaciones_2[3]:.8f} (Valor real: {valor_real_2:.8f})")

# Graficar aproximaciones (descomenta para ver las gráficas)
# graficar_aproximaciones(f1, x0_1, x_objetivo_1, aproximaciones_1, "Aproximaciones de Taylor para f(x) = 0.3x³ - 1.8x² + 2.5x - 1")
# graficar_aproximaciones(f2, x0_2, x_objetivo_2, aproximaciones_2, "Aproximaciones de Taylor para f(x) = 1.4e^x - 3.2x + 2.4")