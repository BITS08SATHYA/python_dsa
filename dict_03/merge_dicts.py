
def merge_dicts(dict1, dict2):

    if len(dict1) & len(dict2) == 0:
        return -1

    union_keys = dict1.keys() | dict2.keys()

    result_dict = {}

    for key in union_keys:
        if key in dict1 and key in dict2:
            result_dict[key] = dict1[key] + dict2[key]
        elif key in dict1:
            result_dict[key] = dict1[key]
        elif key in dict2:
            result_dict[key] = dict2[key]

    return result_dict


def merge_dict_simple(dict1, dict2):
    result = dict1.copy()
    for key,value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
# print(merge_dicts(dict1, dict2))
print(merge_dict_simple(dict1, dict2))