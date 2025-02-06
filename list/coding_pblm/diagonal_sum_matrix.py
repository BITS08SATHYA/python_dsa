import numpy as np

myList2D= [[1,2,3],[4,5,6],[7,8,9]]

def diagonal_sum(matrix):
    # TODO
    diag_sum = 0
    for i in range(len(matrix)):
       diag_sum += matrix[i][i]
    return diag_sum

print(diagonal_sum(myList2D))


