arr1 = [True,False]      
arr2 = [True,False,True]  

def compare(arr1, arr2):
    
    if len(arr1) != len(arr2):
        return False

    for element1, element2 in zip(arr1, arr2):
        if element1 != element2:
            return False  

    return True
            
print(compare(arr1,arr2))
