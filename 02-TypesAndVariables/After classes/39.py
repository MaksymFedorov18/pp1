price= float(input('Enter price: '))
discount= float(input('Enter discount (%): '))
discount_true= discount / 100
reduction= discount_true * price
total= price - reduction
print(f'Price with discount:{total:.2f}')
print(f'Reduction:{reduction:.2f}')