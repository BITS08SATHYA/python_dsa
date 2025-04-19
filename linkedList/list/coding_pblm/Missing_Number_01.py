def equicheck(x, arr):
    if x not in arr:
        return x


def missing_number(arr, n):
    ideal_sum = n*(n+1) // 2
    actual_sum = sum(arr)
    return ideal_sum - actual_sum



print(missing_number([1,2,3,4,6], 6))