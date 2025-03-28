def eliminacion_gauss_jordan(matriz):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for fila_pivote in range(filas):
        # Encontrar un pivote no nulo
        elemento_maximo = 0
        fila_maxima = fila_pivote
        
        # Buscar la fila con el valor absoluto más grande en la columna actual
        for r in range(fila_pivote, filas):
            if abs(matriz[r][fila_pivote]) > elemento_maximo:
                elemento_maximo = abs(matriz[r][fila_pivote])
                fila_maxima = r
        
        # Intercambiar filas si el pivote actual es cero
        if fila_maxima != fila_pivote:
            matriz[fila_pivote], matriz[fila_maxima] = matriz[fila_maxima], matriz[fila_pivote]
        
        # Saltar si el pivote sigue siendo cero después del intercambio
        if matriz[fila_pivote][fila_pivote] == 0:
            continue
        
        # Normalizar la fila actual
        pivote = matriz[fila_pivote][fila_pivote]
        for j in range(fila_pivote, columnas):
            matriz[fila_pivote][j] /= pivote
        
        # Eliminar la variable actual de otras filas
        for i in range(filas):
            if i != fila_pivote:
                factor = matriz[i][fila_pivote]
                for j in range(fila_pivote, columnas):
                    matriz[i][j] -= factor * matriz[fila_pivote][j]
    
    return matriz

def resolver_sistema_lineal(matriz):
   
    # Realizar eliminación de Gauss-Jordan
    matriz_reducida = eliminacion_gauss_jordan(matriz)
    
    # Verificar sistemas inconsistentes o indeterminados
    for i in range(len(matriz_reducida)):
        # Verificar si una fila es todos ceros excepto la última columna (sistema inconsistente)
        if all(abs(matriz_reducida[i][j]) < 1e-10 for j in range(len(matriz_reducida[i])-1)) and abs(matriz_reducida[i][-1]) > 1e-10:
            return "Sistema inconsistente (sin solución)"
    
    # Extraer solución
    solucion = [round(fila[-1], 4) for fila in matriz_reducida]
    return solucion

# Sistema de ecuaciones del problema
sistema = [
    [2, 0, 2, 7],    # 2x1 + 2x3 = 7
    [4, 0, -1, 18],  # 4x1 - x3 = 18
    [3, 2, -2, 16]   # 3x1 + 2x2 - 2x3 = 16
]

# Resolver el sistema
resultado = resolver_sistema_lineal(sistema)
print("Solución:", resultado)