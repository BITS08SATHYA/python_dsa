def reverse_dict(dict):

    reverse_dict = {}
    for key,value in dict.items():
        reverse_dict[value] = key
    return reverse_dict

def reverse_dict_1(dict):
    return {v:k for k,v in dict.items()}

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))