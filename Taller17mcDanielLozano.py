import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x, y):
   
    n = len(x)
    
    # Calcular sumas necesarias
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sum_x_squared = sum(x_i**2 for x_i in x)
    
    # Calcular medias
    mean_x = sum_x / n
    mean_y = sum_y / n
    
    # Calcular coeficientes
    a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a0 = mean_y - a1 * mean_x
    
    return a0, a1

def plot_regression(x, y, a0, a1):
    """
    Grafica los puntos de datos y la línea de regresión.
    """
    plt.figure(figsize=(10, 6))
    
    # Graficar puntos de datos
    plt.scatter(x, y, color='blue', label='Datos')
    
    # Crear línea de regresión
    x_line = np.linspace(min(x), max(x), 100)
    y_line = a0 + a1 * x_line
    
    # Graficar línea de regresión
    plt.plot(x_line, y_line, color='red', label=f'y = {a0:.3f} + {a1:.3f}x')
    
    # Calcular el error cuadrático medio
    y_pred = [a0 + a1 * x_i for x_i in x]
    mse = sum((y_i - y_pred_i)**2 for y_i, y_pred_i in zip(y, y_pred)) / len(y)
    
    plt.title(f'Regresión Lineal por Mínimos Cuadrados\nError Cuadrático Medio: {mse:.4f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    # Datos del problema
    x = [0, 1, 2, 3, 4, 5, 6, 7]
    y = [7.5, 5.5, 6.5, 3.5, 4.5, 3, 2.5, 1]
    
    # Calcular los coeficientes de la regresión
    a0, a1 = linear_regression(x, y)
    
    # Mostrar tabla de cálculos
    print("Cálculos para la regresión lineal:")
    print("----------------------------------")
    print(f"{'X':<5} {'Y':<5} {'XY':<8} {'X²':<5}")
    
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_squared = 0
    
    for x_i, y_i in zip(x, y):
        xy = x_i * y_i
        x_squared = x_i**2
        
        print(f"{x_i:<5} {y_i:<5} {xy:<8} {x_squared:<5}")
        
        sum_x += x_i
        sum_y += y_i
        sum_xy += xy
        sum_x_squared += x_squared
    
    print("----------------------------------")
    print(f"∑X = {sum_x}")
    print(f"∑Y = {sum_y}")
    print(f"∑XY = {sum_xy}")
    print(f"∑X² = {sum_x_squared}")
    print(f"n = {len(x)}")
    print(f"X̄ = {sum_x/len(x)}")
    print(f"Ȳ = {sum_y/len(x)}")
    print("----------------------------------")
    
    # Mostrar la ecuación de la recta
    print(f"Coeficientes de la regresión: a0 = {a0:.4f}, a1 = {a1:.4f}")
    print(f"Ecuación de la recta: y = {a0:.4f} + ({a1:.4f})x")
    
    # Graficar la regresión
    plot_regression(x, y, a0, a1)

if __name__ == "__main__":
    main()