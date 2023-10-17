phone_number= input('Enter phone number: ')
if len(phone_number) != 9 or not phone_number.isdigit():
    print("Invalid input. Please enter a 9-digit number.")
else:
    formatted_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
    print(f'Phone number:{formatted_number}')