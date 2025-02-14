def insert_value_front(input_tuple, value):
    return (value,) + input_tuple

input_tuple = (1,2,3,4)
value = -1
print(insert_value_front(input_tuple, value))