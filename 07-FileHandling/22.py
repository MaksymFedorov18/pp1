import random

with open("numbers.txt" , "w")as file:
    for number in range(50):
        random_number = random.randint(100,990)
        file.write(f"{random_number}\n")