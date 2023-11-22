def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr




arr1 = [64, 34, 25, 12, 22, 11, 90]
sorted_arr1 = bubblesort(arr1)
print("Sorted array 1:", sorted_arr1)


arr2 = [5, 2, 9, 1, 5, 6]
sorted_arr2 = bubblesort(arr2)
print("Sorted array 2:", sorted_arr2)


arr3 = [99, 88, 77, 66, 55, 44, 33, 22, 11]
sorted_arr3 = bubblesort(arr3)
print("Sorted array 3:", sorted_arr3)
