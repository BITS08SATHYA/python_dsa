def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1


my_list = [1,2,3,4,5,59]

print(linear_search(my_list , 59))