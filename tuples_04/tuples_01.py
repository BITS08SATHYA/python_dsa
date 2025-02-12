newTuple = ('a','b','c','d','e')
newTuple1 = tuple('abcde')
# print(newTuple[:3])


# for i in range(len(newTuple)):
#     print(newTuple[i])


# Searching an element in tuple
# print(newTuple.index('a'))


def searchTuple(p_tuple, elt):
    for i in range(len(p_tuple)):
        if p_tuple[i] == elt:
            return f'The {elt} is found at {i} index'
    return 'The elt is not found'

print(searchTuple(newTuple, 'r'))