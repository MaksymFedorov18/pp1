def f(number,even):
    sum= 0
    number_str= str(number)
    for digit in number_str:
        digit= int(digit)
        if (even and digit % 2 == 0) or (not even and digit % 2 != 0):
            sum += digit
    
    return sum

print(f(20586,True)) 
print(f(3124,False)) 
print(f(20576,False)) 
print(f(20576,True)) 
print(f(13115,True)) 
