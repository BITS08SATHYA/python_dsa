
def first_second(list):

    max_1, max_2 =  float('-inf'), float('-inf')

    for num in list:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2 and num != max_1:
            max_2 = num
    return max_1, max_2

my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))
