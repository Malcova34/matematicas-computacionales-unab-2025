import numpy as np
import matplotlib.pyplot as plt

# --- Datos de entrada ---
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_data = np.array([4.5, 6.5, 7.5, 8, 8.4, 8.8, 9, 9.3])
n = len(x_data)

# --- Función genérica para regresión lineal OLS ---
# Recibe los datos transformados (X, Y)
def calculate_ols(X, Y):
    n_ols = len(X)
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    sum_XY = np.sum(X * Y)
    sum_X2 = np.sum(X**2)
    sum_Y2 = np.sum(Y**2)

    # Calcular coeficientes linealizados A1 (pendiente) y A0 (intercepto)
    # Evitar división por cero si el denominador es muy pequeño
    denominator_A1 = n_ols * sum_X2 - sum_X**2
    if np.abs(denominator_A1) < 1e-10: # Umbral pequeño para evitar inestabilidad
        print("Advertencia: Denominador A1 cercano a cero.")
        return None, None, None # O manejar de otra forma

    A1 = (n_ols * sum_XY - sum_X * sum_Y) / denominator_A1
    A0 = (sum_Y / n_ols) - A1 * (sum_X / n_ols)

    # Calcular R^2 usando los datos transformados
    numerator_r2 = (n_ols * sum_XY - sum_X * sum_Y)**2
    denominator_r2_part1 = (n_ols * sum_X2 - sum_X**2)
    denominator_r2_part2 = (n_ols * sum_Y2 - sum_Y**2)

    # Evitar división por cero en R^2
    if np.abs(denominator_r2_part1 * denominator_r2_part2) < 1e-10:
         r2 = 0 # O manejar como indefinido si se prefiere
         print("Advertencia: Denominador R^2 cercano a cero.")
    else:
        r2 = numerator_r2 / (denominator_r2_part1 * denominator_r2_part2)


    return A0, A1, r2

# --- Modelo Lineal ---
def linear_regression(x, y):
    A0, A1, r2 = calculate_ols(x, y)
    if A0 is None: return None, None, None, None # Propagar fallo si calculate_ols falló

    a0 = A0
    a1 = A1
    # Función de predicción
    def predict(x_vals):
        return a0 + a1 * x_vals
    eq_str = f'$y = {a0:.4f} + {a1:.4f}x$' # Formato LaTeX
    return a0, a1, r2, predict, eq_str

# --- Modelo Exponencial ---
def exponential_regression(x, y):
    # Transformación: Y = ln(y), X = x
    Y = np.log(y)
    X = x
    A0, A1, r2 = calculate_ols(X, Y)
    if A0 is None: return None, None, None, None

    # Parámetros originales: a = exp(A0), b = A1
    a = np.exp(A0)
    b = A1
    # Función de predicción
    def predict(x_vals):
        return a * np.exp(b * x_vals)
    eq_str = f'$y = {a:.4f} e^{{{b:.4f}x}}$' # Formato LaTeX
    return a, b, r2, predict, eq_str

# --- Modelo Ecuación de Potencia ---
def power_equation_regression(x, y):
    # Transformación: Y = ln(y), X = ln(x)
    # Asegurarse que no hay x <= 0
    if np.any(x <= 0):
        print("Error: El modelo de ecuación de potencia requiere x > 0.")
        return None, None, None, None
    Y = np.log(y)
    X = np.log(x)
    A0, A1, r2 = calculate_ols(X, Y)
    if A0 is None: return None, None, None, None

    # Parámetros originales: a = exp(A0), b = A1
    a = np.exp(A0)
    b = A1
     # Función de predicción
    def predict(x_vals):
        # Manejar predicción para x > 0
        safe_x_vals = np.maximum(x_vals, 1e-10) # Evitar log(0) o potencia de 0
        return a * (safe_x_vals**b)
    eq_str = f'$y = {a:.4f} x^{{{b:.4f}}}$' # Formato LaTeX
    return a, b, r2, predict, eq_str

# --- Modelo Razón de Crecimiento ---
def growth_rate_regression(x, y):
     # Transformación: Y = 1/y, X = 1/x
    # Asegurarse que no hay x = 0 o y = 0
    if np.any(x == 0) or np.any(y == 0):
        print("Error: El modelo de razón de crecimiento requiere x != 0 y y != 0.")
        return None, None, None, None
    Y = 1 / y
    X = 1 / x
    A0, A1, r2 = calculate_ols(X, Y)
    if A0 is None: return None, None, None, None

    # Parámetros originales: a = 1/A0, b = A1/A0 = A1 * a
    if np.abs(A0) < 1e-10:
        print("Error: A0 cercano a cero en razón de crecimiento, 'a' sería infinito.")
        return None, None, None, None
    a = 1 / A0
    b = A1 * a
    # Función de predicción
    def predict(x_vals):
        # Evitar división por cero en el denominador (b + x_vals)
        denominator = b + x_vals
        # Usar np.where para manejar el caso denominador == 0 (aunque poco probable aquí)
        return np.where(np.abs(denominator) > 1e-10, (a * x_vals) / denominator, np.inf)
    eq_str = f'$y = \\frac{{{a:.4f}x}}{{{b:.4f} + x}}$' # Formato LaTeX
    return a, b, r2, predict, eq_str

# --- Ejecución y Resultados ---
results = {}

# Lineal
params_lin = linear_regression(x_data, y_data)
if params_lin[0] is not None:
    results['Lineal'] = {'params': params_lin[:2], 'R2': params_lin[2], 'predict': params_lin[3], 'eq': params_lin[4]}

# Exponencial
params_exp = exponential_regression(x_data, y_data)
if params_exp[0] is not None:
    results['Exponencial'] = {'params': params_exp[:2], 'R2': params_exp[2], 'predict': params_exp[3], 'eq': params_exp[4]}

# Ecuación Potencia
params_pow = power_equation_regression(x_data, y_data)
if params_pow[0] is not None:
    results['Ecuación Potencia'] = {'params': params_pow[:2], 'R2': params_pow[2], 'predict': params_pow[3], 'eq': params_pow[4]}

# Razón Crecimiento
params_gr = growth_rate_regression(x_data, y_data)
if params_gr[0] is not None:
    results['Razón Crecimiento'] = {'params': params_gr[:2], 'R2': params_gr[2], 'predict': params_gr[3], 'eq': params_gr[4]}

# --- Impresión de Resultados ---
print("--- Resultados de las Regresiones ---")
for name, data in results.items():
    print(f"Modelo {name}:")
    print(f"  Ecuación: {data['eq']}")
    # Imprimir parámetros específicos si se desea (ej: a0, a1 para lineal; a, b para otros)
    # print(f"  Parámetros: {data['params']}") # Descomentar si se quieren ver los parámetros numéricos
    print(f"  Coeficiente de Determinación ($R^2$): {data['R2']:.6f}\n")


# --- Comparación de Modelos ---
if results: # Verificar que hay resultados antes de buscar el máximo
    best_model_name = max(results, key=lambda k: results[k]['R2'])
    best_r2 = results[best_model_name]['R2']
    print(f"\n--- Mejor Ajuste ---")
    print(f"El modelo que mejor se ajusta a los datos es el de '{best_model_name}'")
    print(f"Su coeficiente de determinación ($R^2$) es: {best_r2:.6f}")
else:
    print("\nNo se pudieron calcular los modelos.")


# --- Gráfica Comparativa ---
if results:
    plt.figure(figsize=(12, 7))
    plt.scatter(x_data, y_data, label='Datos Originales', color='red', zorder=5) # Puntos encima

    # Crear un rango de x más suave para las curvas
    x_curve = np.linspace(min(x_data), max(x_data), 200)

    # Graficar cada modelo ajustado
    for name, data in results.items():
        y_curve = data['predict'](x_curve)
        plt.plot(x_curve, y_curve, label=f"{name} ({data['eq']}, $R^2={data['R2']:.4f}$)")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparación de Modelos de Regresión por Mínimos Cuadrados')
    plt.legend(loc='best', fontsize='small') # Ajustar posición y tamaño de leyenda
    plt.grid(True)
    plt.ylim(bottom=0) # Asegurar que el eje y empieza en 0 o cerca si los datos lo permiten
    plt.tight_layout() # Ajustar layout para que no se solapen elementos
    plt.show()