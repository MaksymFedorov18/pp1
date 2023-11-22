arr_1 = [4,36,12,28,9,44,5]
arr_2 = [5,1,36]
empty_list = []
for n in arr_1:
    if n not in arr_2:
        empty_list.append(n)

print(empty_list)