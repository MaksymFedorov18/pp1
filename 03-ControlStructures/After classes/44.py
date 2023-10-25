quantity = 0
total = 0

while True:
    try:
        number = float(input("Enter a number: "))
        if number == 0:
            break  
        total += number
        quantity += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if quantity > 0:
    mean = total / quantity
else:
    mean = 0


print(f"RESULT: Quantity={quantity}, Sum={total}, Mean={mean}")