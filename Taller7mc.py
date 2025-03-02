def solicitar_valor(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if -32768 <= valor <= 32767:
                return valor
            else:
                print("El valor debe estar entre -32,768 y 32,767. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor entero.")

def complemento_a_dos(valor, bits=16):
    if valor < 0:
        valor = (1 << bits) + valor
    return valor

def suma_complemento_a_dos(valor1, valor2, bits=16):
    # Sumar los valores en complemento a dos
    suma = valor1 + valor2
    # Asegurarse de que el resultado esté dentro de 16 bits
    suma = suma & 0xFFFF
    # Si el resultado es mayor que el máximo positivo en 16 bits, es negativo
    if suma & (1 << (bits - 1)):
        suma -= 1 << bits
    return suma

def valor_a_binario(valor, bits=16):
    # Convertir un valor entero a su representación binaria de 16 bits
    return bin(valor & 0xFFFF)[2:].zfill(bits)

def principal():
    # Solicitar los dos valores al usuario
    valor1 = solicitar_valor("Ingrese el primer valor entero entre -32,768 y 32,767: ")
    valor2 = solicitar_valor("Ingrese el segundo valor entero entre -32,768 y 32,767: ")

    # Convertir los valores a complemento a dos de 16 bits
    valor1_comp = complemento_a_dos(valor1)
    valor2_comp = complemento_a_dos(valor2)

    # Mostrar los valores en binario
    print(f"\nPrimer valor en binario (16 bits): {valor_a_binario(valor1_comp)}")
    print(f"Segundo valor en binario (16 bits): {valor_a_binario(valor2_comp)}")

    # Realizar la suma en complemento a dos
    resultado_comp = suma_complemento_a_dos(valor1_comp, valor2_comp)

    # Mostrar el resultado en decimal y binario
    print(f"\nEl resultado de la suma en complemento a dos (decimal) es: {resultado_comp}")
    print(f"El resultado de la suma en complemento a dos (binario) es: {valor_a_binario(resultado_comp)}")

if __name__ == "__main__":
    principal()
