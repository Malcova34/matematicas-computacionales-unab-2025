# Función para leer un conjunto y validar su cardinalidad
def leer_conjunto(nombre):
    n = int(input(f"Ingrese la cardinalidad del conjunto {nombre}: "))
    elementos = []
    for i in range(n):
        elem = input(f"Ingrese el elemento {i+1} de {nombre}: ").strip()
        elementos.append(elem)
    conjunto = set(elementos)
    if len(conjunto) != n:
        print(f"Error: El conjunto {nombre} contiene elementos duplicados.")
        exit()
    return conjunto

# Leer conjuntos U y A
print("Conjunto Universal U:")
U = leer_conjunto("U")

print("\nConjunto A:")
A = leer_conjunto("A")

# Verificar que A sea subconjunto de U
if not A.issubset(U):
    print("\nError: A no es subconjunto de U.")
    exit()

# Realizar las operaciones
op1 = (U & A).union(A)
op2 = U - (A & A)
op3 = (U ^ A) - A

# Función para formatear la salida de conjuntos
def formatear_conjunto(conjunto):
    return "{" + ", ".join(sorted(conjunto)) + "}"

# Mostrar resultados
print("\nResultados de las operaciones:")
print(f"1. (U ∩ A) ∪ A = {formatear_conjunto(op1)}")
print(f"2. U - (A ∩ A) = {formatear_conjunto(op2)}")
print(f"3. (U ⨁ A) - A = {formatear_conjunto(op3)}")