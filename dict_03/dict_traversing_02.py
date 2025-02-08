myDict = {'name':'Sathya', 'age':25,'address':'London'}


# traversing a Dictionary
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

# traverseDict(myDict)


# Searching a Element in dictionary
def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,value
    return 'The value does not exist'

# print(searchDict(myDict,'Sathya1'))

# deleting a element in dictionary
# del myDict['age']
# removed_elt_dict = myDict.pop('age')
# print(removed_elt_dict)

myDict.clear()

print(myDict)
