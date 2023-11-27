with open("power.txt" , "w") as file:
    for number in range(1,11):
        square = number ** 2
        cube = number ** 3
        file.write(f"{number}, {square} , {cube}\n")