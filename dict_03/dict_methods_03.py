myDict = {'name':'Sathya', 'age':25, 'address':'London'}


# clear method
# myDict.clear()
# print(myDict)

# Copy method
dict = myDict.copy()
dict['age'] = 33
# print(dict)
# print(myDict)

# fromKeys
# newDict = {}.fromkeys([1,2,3], 0)
# print(newDict)

# get
# print(myDict.get('city', 27))

# items
# print(myDict.items())

# keys
# print(myDict.keys())

# popItems
# print(myDict.popitem())
# print(myDict)


# setdefault
# print(myDict.setdefault('name1', 'added'))
# print(myDict)

# pop
# print(myDict.pop('name1', 'not'))
# print(myDict)

# values
# print(myDict.values())

# update
newDict = {'a':1, 'b':2, 'c':3}
myDict.update(newDict)
print(myDict)
