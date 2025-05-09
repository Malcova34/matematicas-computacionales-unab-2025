import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x):
    """
    Calcula el valor del polinomio de interpolación de Lagrange en el punto x
    
    Parámetros:
    x_points -- Lista de valores x de los puntos de interpolación
    y_points -- Lista de valores y de los puntos de interpolación
    x -- Punto donde evaluar el polinomio
    
    Retorna:
    El valor del polinomio en x
    """
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        # Calcular el término L_i(x)
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        
        # Añadir al resultado
        result += term
    
    return result

def get_lagrange_polynomial_string(x_points, y_points):
    """
    Genera una representación en string del polinomio de Lagrange
    
    Parámetros:
    x_points -- Lista de valores x de los puntos de interpolación
    y_points -- Lista de valores y de los puntos de interpolación
    
    Retorna:
    String que representa el polinomio
    """
    n = len(x_points)
    # Evaluamos el polinomio en muchos puntos
    x_eval = np.linspace(min(x_points), max(x_points), 1000)
    y_eval = [lagrange_interpolation(x_points, y_points, xi) for xi in x_eval]
    
    # Ajustamos un polinomio a estos puntos
    coefs = np.polyfit(x_eval, y_eval, n-1)
    
    # Formateamos el polinomio como string
    polynomial = "P(x) = "
    for i, coef in enumerate(coefs):
        power = n - 1 - i
        if coef != 0:
            # Formato para el signo
            if i == 0:
                polynomial += f"{coef:.4f}"
            else:
                polynomial += f" + {coef:.4f}" if coef > 0 else f" - {abs(coef):.4f}"
            
            # Añadir la variable x con su potencia
            if power > 1:
                polynomial += f"x^{power}"
            elif power == 1:
                polynomial += "x"
    
    return polynomial

def main():
    # Puntos dados
    x_points = [1, 2, 3, 4, 5]
    y_points = [2, 0.5, -2, -3.5, 0.5]
    
    # Imprimimos la tabla de puntos
    print("Puntos de interpolación:")
    print("x\tf(x)")
    for x, y in zip(x_points, y_points):
        print(f"{x}\t{y}")
    
    # Calculamos y mostramos el polinomio
    poly_string = get_lagrange_polynomial_string(x_points, y_points)
    print("\nPolinomio de interpolación de Lagrange:")
    print(poly_string)
    
    # Generamos puntos para graficar el polinomio
    x_curve = np.linspace(min(x_points) - 0.5, max(x_points) + 0.5, 100)
    y_curve = [lagrange_interpolation(x_points, y_points, x) for x in x_curve]
    
    # Creamos la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x_curve, y_curve, 'b-', label='Polinomio de Lagrange')
    plt.scatter(x_points, y_points, color='red', s=50, label='Puntos dados')
    
    # Añadimos etiquetas y leyenda
    plt.title('Interpolación de Lagrange')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    
    # Añadimos los valores de los puntos en la gráfica
    for i, (x, y) in enumerate(zip(x_points, y_points)):
        plt.annotate(f"({x}, {y})", (x, y), xytext=(5, 5), textcoords='offset points')
    
    # Mostramos la gráfica
    plt.savefig('lagrange_interpolation.png')
    plt.show()

if __name__ == "__main__":
    main()