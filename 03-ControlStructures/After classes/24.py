current_price = float(input("Current product price: "))
previous_price = float(input("Previous product price: "))

percentage_decrease = ((previous_price - current_price) / previous_price) * 100

if percentage_decrease >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {percentage_decrease:.1f}%")
else:
    print('No need to buy')