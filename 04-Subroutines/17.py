n1= int(input('Enter first number: '))
n2= int(input('Enter second number: '))
n3= int(input('Enter third number: '))

def difference(n1,n2,n3):
    return not (n1 == n2 == n3)

is_different = difference(n1, n2, n3)

print(f'Numbers {n1}, {n2}, and {n3} are {"different" if is_different else "not different"}')