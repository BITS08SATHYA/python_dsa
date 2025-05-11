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

# insertionSort(cList)


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

# Time complexity O(NLogN)
def merge(customList, l, m ,r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        j += 1

    while j < n2:
        customList[k] = R[j]
        i += 1
        k += 1

def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r-1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList

# print(mergeSort(cList, 0, 8))


def swap(mylist, index1, index2):
    mylist[index1], mylist[index2] = mylist[index2], mylist[index1]

def pivot(mylist, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist, swap_index, i)
    swap(mylist, pivot_index, swap_index)
    return swap_index

mylist = [2, 1, 4, 5, 7, 8, 4, 3, 1]
# print(pivot(mylist, 0, 8))
# print(mylist)


def quicksort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quicksort_helper(my_list, left, pivot_index - 1)
        quicksort_helper(my_list, pivot_index + 1, right)
    return my_list

def quicksort(my_list):
    return quicksort_helper(my_list, 0, len(my_list) - 1)


# print(quicksort(mylist))

# Time complexity O(NLogN)
# HeapSort
def heapify(mylist, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and mylist[l] < mylist[smallest]:
        smallest = l
    if r < n and mylist[r] < mylist[smallest]:
        smallest = r
    if smallest != i:
        mylist[i], mylist[smallest] = mylist[smallest], mylist[i]
        heapify(mylist, n, smallest)

def heapsort(customList):
    n = len(customList)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)
    for i in range(n-1,0,-1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)

chList = [2,1,7,6,5,3,4,9,8]
heapsort(chList)
print(chList)


