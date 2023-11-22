numbers= [15, 8, 31, 47, 2, 19]
sum = 0
count= 0
while count < len(numbers):
    sum+=numbers[count]
    count+=1

avg = sum / count
print(int(avg))