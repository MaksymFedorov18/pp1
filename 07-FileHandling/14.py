file = open("shopping.txt" , "a")
read_product = True
counter = 0
while read_product:
    product = input("Enter product name: ")
    if product != "-":
        counter += 1
        counter_str = str(counter)
        file.write(f"{counter_str}. {product}\n")
    else:
        read_product = False
