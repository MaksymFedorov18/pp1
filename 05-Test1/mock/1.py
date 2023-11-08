def is_valid_binary(binary_number):
    valid_symbols = {'0', '1'}
    for element in binary_number:
        if element not in valid_symbols:
           
            return False
    
    
    return True

print(is_valid_binary("1010101010"))  
print(is_valid_binary("110201"))      
print(is_valid_binary("111000"))      



        


