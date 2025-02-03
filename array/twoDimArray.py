import numpy as np

# Day 1 - 11, 15,10,6
# Day 2 - 10, 14,11,5
# Day 3 - 12, 17,12,8
# Day 4 - 15, 18,14,9

twoArray = np.array([[11, 15,10,6],[10,14,11,5],[12,17,12,8], [15,18,14,9]  ])
print(twoArray)


# newTwoDArray = np.insert(twoArray,2,[[1,2,3,4]], axis=0)
# print(newTwoDArray)

newTwoDArray = np.append(twoArray,[[1,2,3,4]], axis=0)
print(newTwoDArray)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

# accessElements(twoArray, 1, 2)


def traverseTArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTArray(twoArray)


def searchTArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f'The value is located at index {(i,j)}'
    return 'The element was not found'

print(searchTArray(twoArray, 155))

newTDArray = np.delete(twoArray,0,axis=1)
print(newTDArray)