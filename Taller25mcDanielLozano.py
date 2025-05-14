import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Definición de los puntos de la tabla
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 5, 2.5, 4, -1.6, 2])

# Punto a evaluar
x_eval = 3.55

# MÉTODO 1: POLINOMIO DE INTERPOLACIÓN DE LAGRANGE
def lagrange_interpolation(x_data, y_data, x_punto):
    """
    Calcula el valor del polinomio de interpolación de Lagrange en un punto específico.
    También retorna el polinomio completo como una función.
    """
    n = len(x_data)
    polinomio = 0
    
    for i in range(n):
        # Calculamos el i-ésimo polinomio de Lagrange
        Li = 1
        for j in range(n):
            if j != i:
                Li *= (x_punto - x_data[j]) / (x_data[i] - x_data[j])
        
        # Sumamos al polinomio general
        polinomio += y_data[i] * Li
    
    return polinomio

def obtener_polinomio_lagrange(x_data, y_data):
    """
    Retorna una función que representa el polinomio de Lagrange
    """
    n = len(x_data)
    
    def polinomio(x_punto):
        resultado = 0
        for i in range(n):
            # Coeficiente para el término del polinomio de Lagrange
            L_i = 1
            for j in range(n):
                if j != i:
                    L_i *= (x_punto - x_data[j]) / (x_data[i] - x_data[j])
            resultado += y_data[i] * L_i
        return resultado
    
    return polinomio

# Calculo del polinomio de Lagrange y el valor en x_eval
polinomio_lagrange = obtener_polinomio_lagrange(x, y)
valor_lagrange = lagrange_interpolation(x, y, x_eval)

# MÉTODO 2: TRAZADORES CÚBICOS (CUBIC SPLINES)
# Utilizamos la función CubicSpline de scipy para calcular los trazadores cúbicos
cs = CubicSpline(x, y)

# Valor en el punto de evaluación
valor_spline = cs(x_eval)

# RESULTADOS
print("Resultados:")
print(f"Valor en x = {x_eval} usando Polinomio de Lagrange: {valor_lagrange:.6f}")
print(f"Valor en x = {x_eval} usando Trazadores Cúbicos: {valor_spline:.6f}")

# GRÁFICA
plt.figure(figsize=(12, 8))

# Puntos originales
plt.scatter(x, y, color='red', s=50, label='Puntos originales')

# Punto de evaluación
plt.scatter(x_eval, valor_lagrange, color='green', s=100, label=f'Lagrange en x={x_eval}')
plt.scatter(x_eval, valor_spline, color='blue', s=100, label=f'Spline en x={x_eval}')

# Líneas de interpolación
x_continuo = np.linspace(min(x), max(x), 1000)
y_lagrange = [polinomio_lagrange(xi) for xi in x_continuo]
y_spline = cs(x_continuo)

plt.plot(x_continuo, y_lagrange, 'g-', label='Polinomio de Lagrange')
plt.plot(x_continuo, y_spline, 'b--', label='Trazadores Cúbicos')

# Configuración de la gráfica
plt.title('Interpolación: Polinomio de Lagrange vs Trazadores Cúbicos')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# Información sobre los coeficientes de los trazadores cúbicos
print("\nCoeficientes de los Trazadores Cúbicos (por segmento):")
for i in range(len(x)-1):
    print(f"Segmento {i} (de x={x[i]} a x={x[i+1]}):")
    # Los coeficientes están organizados como:
    # S_i(x) = a*(x-x_i)^3 + b*(x-x_i)^2 + c*(x-x_i) + d
    # En CubicSpline: cs.c[k, i] = coeficiente k del polinomio en el segmento i
    a = cs.c[0, i]  # Coeficiente cúbico
    b = cs.c[1, i]  # Coeficiente cuadrático
    c = cs.c[2, i]  # Coeficiente lineal
    d = cs.c[3, i]  # Término constante
    print(f"  a = {a:.6f}  (coeficiente de (x-{x[i]})^3)")
    print(f"  b = {b:.6f}  (coeficiente de (x-{x[i]})^2)")
    print(f"  c = {c:.6f}  (coeficiente de (x-{x[i]}))")
    print(f"  d = {d:.6f}  (término constante)")

# Mostrar gráfica
plt.tight_layout()
plt.show()

# Para mostrar el polinomio de Lagrange explícitamente
# Vamos a usar sympy para obtener la forma simbólica
from sympy import symbols, expand

def obtener_expresion_lagrange(x_data, y_data):
    """
    Retorna la expresión simbólica del polinomio de Lagrange
    """
    from sympy import symbols, expand
    
    x_sym = symbols('x')
    n = len(x_data)
    polinomio = 0
    
    for i in range(n):
        # Término Li(x)
        numerador = 1
        denominador = 1
        
        for j in range(n):
            if j != i:
                numerador *= (x_sym - x_data[j])
                denominador *= (x_data[i] - x_data[j])
        
        # Sumamos al polinomio
        polinomio += y_data[i] * (numerador / denominador)
    
    return expand(polinomio)

# Obtenemos la expresión del polinomio de Lagrange
expresion_lagrange = obtener_expresion_lagrange(x, y)
print("\nPolinomio de interpolación de Lagrange:")
print(expresion_lagrange)