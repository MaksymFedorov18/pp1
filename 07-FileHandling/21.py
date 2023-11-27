with open("numbers.txt" , "w")as file:
    for number in range(1,51):
        file.write(f"{number}\n")
