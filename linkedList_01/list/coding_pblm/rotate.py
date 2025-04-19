def rotate(matrix):
    # for i in range(3):
    #     for j in sorted(range(3),reverse=True):
    #         print(f'''{matrix[j][i]}''', end=' ')
    #     # print(end='\n')
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))