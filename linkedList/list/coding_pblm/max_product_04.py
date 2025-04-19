def max_product(arr):
    max_product = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
    return max_product

print(max_product([1, 7, 3, 4, 9, 5]))