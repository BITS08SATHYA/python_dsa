import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,18,19,20])

def find_Number(array,Number):
    for i in range(len(array)):
        if array[i] == Number:
            return i
    return -1

print(find_Number(myArray,13))