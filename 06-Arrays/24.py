numbers= [15, 8, 31, 47, 2, 19]
sum = 0
count= len(numbers)
for num in numbers:
    sum+=num

avg = sum / count
print(int(avg))