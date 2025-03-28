import random

def generar_conjunto(cardinalidad):
  
  # No pasa de 31 el máximo número
  if cardinalidad > 31:
    print("La cardinalidad no puede ser mayor que 31.")
    cardinalidad = 31
  return set(random.sample(range(31), cardinalidad))

# Obtener la cardinalidad del usuario
cardinalidad_a = int(input("Introduce la cardinalidad del conjunto A: "))
cardinalidad_b = int(input("Introduce la cardinalidad del conjunto B: "))

# Generar los conjuntos
conjunto_a = generar_conjunto(cardinalidad_a)
conjunto_b = generar_conjunto(cardinalidad_b)

# Mostrar los conjuntos
print("Conjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)

# Realizar operaciones con los conjuntos
union = conjunto_a.union(conjunto_b)
interseccion = conjunto_a.intersection(conjunto_b)
a_menos_b = conjunto_a.difference(conjunto_b)
b_menos_a = conjunto_b.difference(conjunto_a)
diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)

# Mostrar los resultados
print("\nA ∪ B:", union)
print("A ∩ B:", interseccion)
print("A - B:", a_menos_b)
print("B - A:", b_menos_a)
print("A ⨁ B:", diferencia_simetrica)
