import copy

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(f"{a[i][j]:.2f}", end=" ")
        print(f"| {b[i]:.2f}")
    print()

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)

    n = len(b)
    imprimirSistema(a, b, "Matriz inicial")
    
    for i in range(n):
        # Buscar un pivote no cero
        if a[i][i] == 0:
            # Buscar una fila con un valor no cero en la columna actual
            for k in range(i+1, n):
                if a[k][i] != 0:
                    # Intercambiar filas
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    print(f"Intercambiando fila {i} con fila {k}")
                    break
            else:
                # Si no se encuentra un pivote no cero, continuar
                continue
        
        pivote = a[i][i]
        
        # Dividir por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        imprimirSistema(a, b, "División")

        # Reducción
        for k in range(n):
            if i != k:
                # Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
        imprimirSistema(a, b, "Reducción")
    
    return b

# Sistema de ecuaciones proporcionado
a = [[2, 0, 2], [4, 0, -1], [3, 2, -2]]
b = [7, 18, 16]

x = gaussJordan(a, b)

print("Respuesta:")
for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.2f}")

# Pruebas
print("\nPruebas:")
for i in range(len(b)):
    valorAux = b[i]
    for j in range(len(b)):
        valorAux -= a[i][j] * x[j]
    print(f"Test {i + 1} = {valorAux:.2e}")