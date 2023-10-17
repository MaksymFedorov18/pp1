binary_number = input("Enter a four-digit binary number: ")

if len(binary_number) != 4 or not binary_number.isdigit() or set(binary_number) - {'0', '1'}:
    print("Invalid input. Please enter a valid four-digit binary number.")
else:
    decimal_value = int(binary_number, 2)
    print(f"Decimal value: {decimal_value}")