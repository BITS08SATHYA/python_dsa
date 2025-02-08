import random

city_names = ['paris','London','Rome','Berlin','Madrid']

new_dict = {city:random.randint(10,30) for city in city_names}
print(new_dict)

# nd = {new_key:new_value for (key,value) in dict.items()}

abv_25 = {city:temp for (city, temp) in new_dict.items()}
print(abv_25)