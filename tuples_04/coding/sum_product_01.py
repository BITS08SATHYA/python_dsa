def sum_product(input_tuple):
    sum_result = 0
    product_result = 1
    for x in range(len(input_tuple)):
        sum_result += input_tuple[x]
        product_result *= input_tuple[x]
    return sum_result, product_result

input_tuple = (1, 2, 3,4)
print(sum_product(input_tuple))