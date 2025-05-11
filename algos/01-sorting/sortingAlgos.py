import math
cList = [2,1,4,5,7,8,4,3,1]


# Time Complexity - O(n^2)
# Takes two adjacent elements and swap them in multiple for loops until the list has been sorted
def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)

# bubbleSort(customList)

# Time Complexity - O(n^2)
# find the minimum index and swap that respective element with the current element until the list has been sorted
def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

# selectionSort(cList)

# Insertion sort
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList

insertionSort(cList)


# Bucket Sort
def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberofBuckets / maxValue)
        arr[index_b-1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList



