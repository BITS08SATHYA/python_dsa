
num = int(input('How many days temperature?'))
list = []
i = 0
sum = 0
count = 0
while i < num:
    temp = int(input(f'Day{i+1}\'s high temp:'))
    list.append(temp)
    i += 1

for x in list:
    sum += x

average = sum/num
print(f'Average = {average}')

for x in list:
    if x > average:
        count += 1

print(f'{count}day(s) above average')
