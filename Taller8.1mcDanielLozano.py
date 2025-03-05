def decimal_to_hex(decimal_num):
   
    if decimal_num == 0:
        return "0"
    
    # Hex digits mapping
    hex_digits = "0123456789ABCDEF"
    
    # Handle negative numbers
    is_negative = decimal_num < 0
    decimal_num = abs(decimal_num)
    
    # Store the hex digits
    hex_result = []
    
    # Successive divisions
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_result.insert(0, hex_digits[remainder])
        decimal_num //= 16
    
    # Add negative sign if original number was negative
    return ("-" if is_negative else "") + "".join(hex_result)

def main():
    try:
        # Pedir al usuario que introduzca un número decimal
        decimal_num = int(input("Introduce un número decimal para convertir a hexadecimal: "))
        
        # Convertir y mostrar el resultado
        hex_result = decimal_to_hex(decimal_num)
        print(f"{decimal_num} (base 10) = {hex_result} (base 16)")
    
    except ValueError:
        print("Error: Introduce un número entero válido.")

if __name__ == "__main__":
    main()