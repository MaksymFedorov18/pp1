number = int(input("Number: "))
array = [15, 38, 7, 23, 14]

def occurs(number, array):
    for num in array:
        if num == number:
            print(f"Array: {array}")
            print(f"Result: number {number} appears in the array")
            return

    print(f"Array: {array}")
    print(f"Result: number {number} does not appear in the array")

occurs(number, array)


    
 
    