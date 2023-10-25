number_of_products= int(input('Number of products purchased: '))
product_price= float(input('Product price: '))
if number_of_products < 2:
    print("Discount can't be applied")
else:
    decrease= product_price * 0.25
    total= (product_price - decrease) * number_of_products
    print(f"Amount to pay:{total:.2f}")