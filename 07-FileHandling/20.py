file_all = open("allproducts.txt", "w")

with open("GrainsAndBread.txt", "r") as file_bread:
    file_content = file_bread.read()
    file_all.write(file_content)

with open("MeatAndFish.txt", "r") as file_meat:
     file_content_1 = file_meat.read()
     file_all.write(file_content_1)

file_all.close()