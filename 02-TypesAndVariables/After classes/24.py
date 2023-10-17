registration= input('Enter vehicle registration number: ')
valid= registration.startswith('KR') or registration.startswith('KK')
print(valid)