import random

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(6)]
arr8 = [[2 for i in range(3)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr10= [4,0,3]
arr11 = [0 for i in range(15)]
arr12 = [random.randint(1,30) for i in range(5)]
arr13 = [random.randint(0,1) for i in range(20)]
two_dimensional_array = [[False] * 2 for i in range(5)]


for row in two_dimensional_array:
    print(row)


