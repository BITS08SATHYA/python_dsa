prev_list = [1,2,3,4,7,2]
new_list = []

for i in prev_list:
    new_list.append(i)

new_list_1 = [new_item**2 for new_item in prev_list]




print(new_list_1)



prev_list_1 = [-1, 10, -20, 2, -90, 60, 45, 20]

new_list_2 = [new_item*new_item for new_item in prev_list_1 if new_item < 0]

print(new_list_2)

sentence = 'My Name is Sathya'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)


def get_number(number):
    if number > 0:
        return number
    else:
        return 'negative number'

new_list_3 = [get_number(number) for number in prev_list]
print(new_list_3)