def max_value(dict):

    max_key = max(dict, key = dict.get)
    return max_key


my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value(my_dict))