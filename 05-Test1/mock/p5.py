def f(binary_number):
    valid_symbols = {'0', '1'}
    return all(char in valid_symbols for char in binary_number)

print(f("101101"))    
print(f("1311a10100")) 
