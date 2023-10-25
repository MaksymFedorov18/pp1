amount= int(input('Enter the amount in PLN: '))
five_zl= 0
two_zl= 0
one_zl= 0

while amount > 0:
    if amount >= 5:
        five_zl += amount // 5
        amount %= 5
    elif amount >= 2:
        two_zl += amount // 2
        amount %= 2
    else:
        one_zl= amount
        break

print('The amount of PLN 18 in coins:')
print(f'5 zł - {five_zl}')
print(f'2 zł - {two_zl}')
print(f'1 zł - {one_zl}')