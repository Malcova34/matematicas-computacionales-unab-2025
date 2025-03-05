def is_valid_octal(octal_str):
   
    # Check if the string contains only digits from 0-7
    return all(digit in '01234567' for digit in octal_str)

def octal_to_decimal(octal_str):
   
    # Check for validity first
    if not is_valid_octal(octal_str):
        print(f"Error: {octal_str} no es un número octal válido")
        return None
    
    # Handle negative numbers
    is_negative = octal_str.startswith('-')
    if is_negative:
        octal_str = octal_str[1:]
    
    # Convert using successive powers
    decimal_num = 0
    power = 0
    
    # Iterate from right to left
    for digit in reversed(octal_str):
        decimal_num += int(digit) * (8 ** power)
        power += 1
    
    # Apply negative sign if needed
    return -decimal_num if is_negative else decimal_num

def main():
    # Pedir al usuario que introduzca un número octal
    octal_input = input("Introduce un número octal para convertir a decimal: ")
    
    # Convertir y mostrar el resultado
    result = octal_to_decimal(octal_input)
    if result is not None:
        print(f"{octal_input} (base 8) = {result} (base 10)")

if __name__ == "__main__":
    main()