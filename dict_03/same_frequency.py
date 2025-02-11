def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for elt in lst:
            counter[elt] = counter.get(elt, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)



list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))