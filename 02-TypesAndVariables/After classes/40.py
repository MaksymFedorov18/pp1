card_number= (input('Enter credit card number: '))
if len(card_number) != 16 :
 print('Invalid input. Please enter a 16-digit card number.')
else:
 formatted= f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}'
 print(f'Card number:{formatted}')