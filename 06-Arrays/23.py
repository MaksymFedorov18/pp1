numbers = [-15, 8, -31, 47, -2, 19]

maximum = numbers[0]
minimum = numbers[0]


for num in numbers:
    if num > maximum:
        maximum = num
    elif num < minimum:
        minimum = num


print("Array:", numbers)
print("Maximum number:", maximum)
print("Minimum number:", minimum)
