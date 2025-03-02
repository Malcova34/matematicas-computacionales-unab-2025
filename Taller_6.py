import math

def factorial(n):
    """Calcula el factorial de un número."""
    return 1 if n == 0 else n * factorial(n - 1)

def cos_taylor(x, es=0.5 * 10**-8 * 100):
    """
    Calcula el coseno de x usando la serie de Taylor hasta que el error sea menor que el criterio es.
    """
    iteraciones = 0
    cos_aprox = 0
    termino = 1  # Primer término de la serie
    n = 0  # Contador de términos
    
    while abs(termino) > es:
        cos_aprox += termino
        n += 1
        termino = (-1)**n * (x**(2*n)) / factorial(2*n)
        iteraciones += 1
        
    error_aproximado = abs(termino / cos_aprox) * 100
    return cos_aprox, error_aproximado, iteraciones

# Entrada del usuario
grado = float(input("Ingrese el valor en radianes: "))
cos_aproximado, error, iteraciones = cos_taylor(grado)

# Mostrar resultados
print(f"Cos({grado}) ≈ {cos_aproximado}")
print(f"Error aproximado relativo porcentual: {error:.8f}%")
print(f"Número de iteraciones: {iteraciones}")
