import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import stats

# Datos proporcionados
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([0, 0.5, 2, 3.5, 4.5, 9, 13.5])

# Cálculo de la recta de regresión por mínimos cuadrados
a1, a0, r, p_value, std_err = stats.linregress(x, y)

# Valores predichos por la recta de regresión
y_pred = a0 + a1 * x

# Cálculo de los residuos
residuos = y - y_pred

# Cálculo de Sy (desviación estándar de y)
y_mean = np.mean(y)
S_t = np.sum((y - y_mean) ** 2)
s_y = np.sqrt(S_t / (len(y) - 1))

# Cálculo de Sy/x (error estándar de la estimación)
S_r = np.sum(residuos ** 2)
s_y_x = np.sqrt(S_r / (len(y) - 2))

# Cálculo del coeficiente de determinación (r²)
r_squared = r ** 2

# Impresión de resultados
print("Resultados de la Regresión Lineal:")
print(f"Ecuación de la recta: y = {a0:.4f} + {a1:.4f}x")
print(f"Desviación estándar (s_y): {s_y:.4f}")
print(f"Error estándar de la estimación (s_y/x): {s_y_x:.4f}")
print(f"Coeficiente de determinación (r²): {r_squared:.4f}")
print(f"Coeficiente de correlación (r): {r:.4f}")

# Creación de la gráfica
plt.figure(figsize=(10, 8))

# Configuración de estilo de gráfica
plt.style.use('seaborn-v0_8-whitegrid')

# Gráfica de dispersión
plt.scatter(x, y, color='blue', label='Datos', s=50)

# Línea de regresión
x_line = np.linspace(-0.5, 6.5, 100)
y_line = a0 + a1 * x_line
plt.plot(x_line, y_line, color='red', label=f'y = {a0:.2f} + {a1:.2f}x')

# Líneas de error
for i in range(len(x)):
    plt.plot([x[i], x[i]], [y[i], y_pred[i]], 'g--', alpha=0.7)

# Títulos y etiquetas
plt.title('Regresión Lineal por Mínimos Cuadrados', fontsize=16)
plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)

# Configuración de la cuadrícula
plt.grid(True, linestyle='--', alpha=0.7)

# Configuración de los límites de los ejes
plt.xlim(-0.5, 6.5)
plt.ylim(-1, 15)

# Configuración de los intervalos de los ejes
plt.gca().xaxis.set_major_locator(MultipleLocator(1))

# Configuración de la leyenda
plt.legend(fontsize=12, loc='upper left')

# Información estadística en el gráfico
info_text = f'$r^2 = {r_squared:.4f}$\n$r = {r:.4f}$\n$s_y = {s_y:.4f}$\n$s_{{y/x}} = {s_y_x:.4f}$'
plt.annotate(info_text, xy=(0.05, 0.95), xycoords='axes fraction', 
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
             fontsize=12, ha='left', va='top')

# Mostrar gráfica
plt.tight_layout()
plt.show()

# Gráfica de residuos
plt.figure(figsize=(10, 6))
plt.scatter(x, residuos, color='green', s=50)
plt.axhline(y=0, color='r', linestyle='-')
plt.title('Gráfica de Residuos', fontsize=16)
plt.xlabel('X', fontsize=14)
plt.ylabel('Residuos (y - ŷ)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()