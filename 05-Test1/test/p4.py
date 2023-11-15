def f(n):
    line= str(n)
    for number in line:
        if number %2 == 0:
            even_number = str(number)
            even_number_str = even_number + '+'
            
        else:
            odd_number = str(number) 
            odd_number_str = odd_number + '++'
            
    total= 1

print(f(23456))