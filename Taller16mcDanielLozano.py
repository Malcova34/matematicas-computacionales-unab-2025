import numpy as np

def gauss_jordan_inverse(matrix):
    """
    Calcula la inversa de una matriz utilizando el método de eliminación de Gauss-Jordan.
    """
    n = len(matrix)
    # Crear una matriz aumentada [A|I]
    augmented = np.hstack((matrix, np.identity(n)))
    
    # Aplicar eliminación de Gauss-Jordan
    for i in range(n):
        # Dividir la fila i por el elemento pivote
        pivot = augmented[i, i]
        augmented[i] = augmented[i] / pivot
        
        # Eliminar el elemento i de las otras filas
        for j in range(n):
            if j != i:
                factor = augmented[j, i]
                augmented[j] = augmented[j] - factor * augmented[i]
    
    # Extraer la matriz inversa
    inverse = augmented[:, n:]
    return inverse

def verify_inverse(matrix, inverse):
    """
    Verifica si la matriz multiplicada por su inversa da como resultado
    una matriz identidad (o muy cercana debido a errores de redondeo).
    """
    product = np.matmul(matrix, inverse)
    identity = np.identity(len(matrix))
    
    # Redondear para evitar problemas con números muy pequeños
    product = np.round(product, decimals=10)
    
    print("Producto de matriz original × inversa:")
    print(product)
    
    is_identity = np.allclose(product, identity, rtol=1e-10)
    return is_identity

def main():
    # Definir las matrices A y B
    A = np.array([
        [3, 2, 2],
        [3, 1, -3],
        [1, 0, -2]
    ])
    
    B = np.array([
        [1, 2, 0, 4],
        [2, 0, -1, -2],
        [1, 1, -1, 0],
        [0, 4, 1, 0]
    ])
    
    # Calcular inversas usando el método de Gauss-Jordan
    print("=== Matriz A ===")
    print("Matriz original:")
    print(A)
    
    A_inv = gauss_jordan_inverse(A)
    print("\nMatriz inversa calculada con Gauss-Jordan:")
    print(A_inv)
    
    # Verificar si A × A⁻¹ = I
    print("\nVerificación:")
    if verify_inverse(A, A_inv):
        print("✓ La matriz inversa es correcta (A × A⁻¹ = I)")
    else:
        print("✗ La matriz inversa no es correcta")
    
    print("\n=== Matriz B ===")
    print("Matriz original:")
    print(B)
    
    B_inv = gauss_jordan_inverse(B)
    print("\nMatriz inversa calculada con Gauss-Jordan:")
    print(B_inv)
    
    # Verificar si B × B⁻¹ = I
    print("\nVerificación:")
    if verify_inverse(B, B_inv):
        print("✓ La matriz inversa es correcta (B × B⁻¹ = I)")
    else:
        print("✗ La matriz inversa no es correcta")
    
    # Verificación adicional usando NumPy
    print("\n=== Verificación con NumPy ===")
    print("Inversa de A usando NumPy:")
    A_inv_np = np.linalg.inv(A)
    print(A_inv_np)
    print("Inversa de B usando NumPy:")
    B_inv_np = np.linalg.inv(B)
    print(B_inv_np)

if __name__ == "__main__":
    main()