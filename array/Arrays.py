from array import *

arr1 = array('i',[1,2,3,4,5])
arr2 = array('d',[1.1,2.1,3.1,4.1,5.1])



def traverseArray(arr):
    for i in arr:
        print(i)


# traverseArray(arr2)


# accessElement
def  accessElement(arr, index):
    if index >= len(arr):
        print('Index out of range')
    else:
        print(f"The element {arr[index]} found at index {index}")

accessElement(arr1,2)

def searchElement(arr, element):
    for i in arr:
        if arr[i] == element:
            return i
    return -1

print(searchElement(arr1,2))


arr1.remove(3)
print(arr1)

