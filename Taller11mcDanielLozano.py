import numpy as np
import pandas as pd
from tabulate import tabulate

# Definición de la función y sus derivadas analíticas
def f(x):
    return 0.25 * x**4 - 0.75 * x**2 + 4.5

def df_dx(x):
    return x**3 - 1.5*x

def d2f_dx2(x):
    return 3 * x**2 - 1.5

# Punto de evaluación y tamaños de paso
x = 0.6
h1 = 0.1
h2 = 0.05

# Calcular valores de función necesarios para h = 0.1
f_x = f(x)
f_x_plus_h = f(x + h1)
f_x_minus_h = f(x - h1)
f_x_plus_2h = f(x + 2*h1)
f_x_minus_2h = f(x - 2*h1)

# Calcular valores para h = 0.05 (solo para diferencias centradas)
f_x_plus_h_small = f(x + h2)
f_x_minus_h_small = f(x - h2)

# ---- Aproximaciones para la primera derivada con h = 0.1 ----

# Diferencia hacia adelante
df_adelante = (f_x_plus_h - f_x) / h1

# Diferencia hacia atrás
df_atras = (f_x - f_x_minus_h) / h1

# Diferencia centrada
df_centrada = (f_x_plus_h - f_x_minus_h) / (2 * h1)

# ---- Aproximaciones para la segunda derivada con h = 0.1 ----

# Diferencia hacia adelante
d2f_adelante = (f_x_plus_2h - 2*f_x_plus_h + f_x) / h1**2

# Diferencia hacia atrás
d2f_atras = (f_x - 2*f_x_minus_h + f_x_minus_2h) / h1**2

# Diferencia centrada
d2f_centrada = (f_x_plus_h - 2*f_x + f_x_minus_h) / h1**2

# ---- Cálculo con h = 0.05 para diferencias centradas ----
df_centrada_h2 = (f_x_plus_h_small - f_x_minus_h_small) / (2 * h2)
d2f_centrada_h2 = (f_x_plus_h_small - 2*f_x + f_x_minus_h_small) / h2**2

# Cálculo de los valores exactos
df_exacta = df_dx(x)
d2f_exacta = d2f_dx2(x)

# ---- Cálculo de errores absolutos ----
error_df_adelante = abs(df_adelante - df_exacta)
error_df_atras = abs(df_atras - df_exacta)
error_df_centrada = abs(df_centrada - df_exacta)
error_df_centrada_h2 = abs(df_centrada_h2 - df_exacta)

error_d2f_adelante = abs(d2f_adelante - d2f_exacta)
error_d2f_atras = abs(d2f_atras - d2f_exacta)
error_d2f_centrada = abs(d2f_centrada - d2f_exacta)
error_d2f_centrada_h2 = abs(d2f_centrada_h2 - d2f_exacta)

# ---- Mostrar resultados ----
print(f"Función: f(x) = 0.25x⁴ - 0.75x² + 4.5")
print(f"Punto de evaluación: x = {x}")
print(f"Valores: f({x}) = {f_x:.6f}")
print("\n")

# Crear DataFrames para mostrar los resultados organizadamente
df_primera = pd.DataFrame({
    'Método': ['Hacia adelante', 'Hacia atrás', 'Centrada (h=0.1)', 'Centrada (h=0.05)', 'Valor exacto'],
    'Valor': [df_adelante, df_atras, df_centrada, df_centrada_h2, df_exacta],
    'Error absoluto': [error_df_adelante, error_df_atras, error_df_centrada, error_df_centrada_h2, 0]
})

df_segunda = pd.DataFrame({
    'Método': ['Hacia adelante', 'Hacia atrás', 'Centrada (h=0.1)', 'Centrada (h=0.05)', 'Valor exacto'],
    'Valor': [d2f_adelante, d2f_atras, d2f_centrada, d2f_centrada_h2, d2f_exacta],
    'Error absoluto': [error_d2f_adelante, error_d2f_atras, error_d2f_centrada, error_d2f_centrada_h2, 0]
})

print("PRIMERA DERIVADA:")
print(tabulate(df_primera, headers='keys', tablefmt='pretty', floatfmt='.8f'))
print("\n")

print("SEGUNDA DERIVADA:")
print(tabulate(df_segunda, headers='keys', tablefmt='pretty', floatfmt='.8f'))

# Análisis de resultados
print("\nANÁLISIS DE RESULTADOS:")
print("-----------------------")

# Comparación de precisión entre h=0.1 y h=0.05 para diferencias centradas
mejora_primera = error_df_centrada / error_df_centrada_h2
mejora_segunda = error_d2f_centrada / error_d2f_centrada_h2

print(f"1. Para la primera derivada, el error con h=0.05 es {mejora_primera:.2f} veces menor que con h=0.1")
print(f"2. Para la segunda derivada, el error con h=0.05 es {mejora_segunda:.2f} veces menor que con h=0.1")

# Verificación del orden de error
print("\nVerificación del orden de error:")
print(f"- Para diferencias centradas en la primera derivada, al reducir h a la mitad, el error debería reducirse aproximadamente a 1/4 (O(h²)): {mejora_primera:.2f} ≈ 4")
print(f"- Para diferencias centradas en la segunda derivada, al reducir h a la mitad, el error debería reducirse aproximadamente a 1/4 (O(h²)): {mejora_segunda:.2f} ≈ 4")

print("\nConclusión:")
if mejora_primera > 3.5 and mejora_segunda > 3.5:
    print("Los resultados confirman que las diferencias centradas tienen un orden de error O(h²),")
    print("ya que al reducir el tamaño de paso a la mitad, el error se reduce aproximadamente a 1/4.")
print("Las diferencias centradas producen resultados más precisos que las diferencias hacia adelante o hacia atrás.")