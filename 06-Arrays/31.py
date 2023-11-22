def unique(array):
    unique_list = []
    seen_set = set()
    repeated_set = set()

    for element in array:
        if element not in seen_set:
            seen_set.add(element)
        else:
            repeated_set.add(element)

    unique_list = list(seen_set - repeated_set)
    return unique_list

arr_1 = [2, 3, 2, 5, 8, 1, 9, 8]
print("Array:", arr_1)
print("Unique elements:", unique(arr_1))
