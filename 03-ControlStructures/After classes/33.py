decimal_number_str = input('Enter decimal number: ')
decimal_number = int(decimal_number_str)
binary_digits = []

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_digits.append(str(remainder))
    decimal_number //= 2

binary_number = ''.join(reversed(binary_digits))
print(f"{decimal_number_str}(10) = {binary_number}(2)")