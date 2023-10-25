# Initialize variables
rows = 7  
columns = 7  
number = 1  

for row in range(rows):
    for column in range(columns):
        print(f'{number:2}', end=' ')
        number += 7
    print()
    number = row + 2
