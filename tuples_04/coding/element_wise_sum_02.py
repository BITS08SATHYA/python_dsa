def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        return ValueError("Input  tuples must have the same length")
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return result

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)