import numpy as np

def producto_punto_vector():
    """
    Crear dos vectores aleatorios de longitud especificada por el usuario y calcular su producto punto
    """
    # Solicitar longitud del vector al usuario
    while True:
        try:
            n = int(input("Ingrese la longitud de los vectores (n): "))
            if n <= 0:
                print("La longitud debe ser un entero positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    # Generar vectores aleatorios
    vector_a = np.random.randint(-10, 11, n)  # Números enteros aleatorios entre -10 y 10
    vector_b = np.random.randint(-10, 11, n)

    # Calcular producto punto
    producto_punto = np.dot(vector_a, vector_b)

    print("\nVector A:", vector_a)
    print("Vector B:", vector_b)
    print("Producto Punto:", producto_punto)

def operaciones_matrices():
    """
    Realizar suma o multiplicación de matrices generadas aleatoriamente
    """
    # Elegir operación
    while True:
        operacion = input("Elija la operación (suma/multiplicar): ").lower()
        if operacion in ['suma', 'multiplicar']:
            break
        print("Operación inválida. Por favor, elija 'suma' o 'multiplicar'.")

    # Generar dimensiones de matrices aleatorias
    m = np.random.randint(2, 9)  # filas para la primera matriz
    n = np.random.randint(2, 9)  # columnas para la primera matriz/filas para la segunda
    p = np.random.randint(2, 9)  # columnas para la segunda matriz

    # Ajustar dimensiones para multiplicación si es necesario
    if operacion == 'multiplicar':
        # Asegurar que la multiplicación de matrices sea posible
        n = m  # asegurar que columnas de A = filas de B

    # Generar matrices aleatorias
    matriz_a = np.random.randint(-10, 11, (m, n))
    matriz_b = np.random.randint(-10, 11, (n, p))

    print("\nMatriz A:")
    print(matriz_a)
    print("\nMatriz B:")
    print(matriz_b)

    # Realizar operación seleccionada
    if operacion == 'suma':
        # Asegurar que las matrices tengan las mismas dimensiones para la suma
        if m == matriz_b.shape[0] and n == matriz_b.shape[1]:
            resultado = matriz_a + matriz_b
            print("\nSuma de Matrices:")
            print(resultado)
        else:
            print("Las matrices deben tener las mismas dimensiones para la suma.")
    else:  # multiplicación
        resultado = np.dot(matriz_a, matriz_b)
        print("\nResultado de Multiplicación de Matrices:")
        print(resultado)

def main():
    print("Operaciones de Vectores y Matrices")
    print("1. Producto Punto de Vectores")
    print("2. Operaciones con Matrices")
    
    while True:
        try:
            eleccion = int(input("\nIngrese su elección (1/2): "))
            if eleccion == 1:
                producto_punto_vector()
            elif eleccion == 2:
                operaciones_matrices()
            else:
                print("Elección inválida. Por favor, ingrese 1 o 2.")
                continue
            
            # Preguntar si desea continuar
            continuar = input("\n¿Desea realizar otra operación? (sí/no): ").lower()
            if continuar != 'sí':
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()