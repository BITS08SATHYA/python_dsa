def pairs_sum(myList, sum):
    output = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                str = f'''{myList[i]}+{myList[j]}'''
                output.append(str)
    return output


print(pairs_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))