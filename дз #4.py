print('\nTask 1\n')

list_0 = [ ]
number = 0
while  number < 100:
    if number % 5 == 0 and number % 7 == 0:
        list_0.append(number)
    number += 1
print(list_0)

print('\nTask 2\n')

list_1 = [2,4,7,84,598,6378]
index = 0
sum = 0
while index != len(list_1):
    sum = sum + int(list_1[index])
    index += 1
print(f'sum of all elements of list_1 = {sum}')

print('\nTask 3\n')

given_list = [False, 0, 'str', '123', 'hello', '%', 1.2, 1]

index = 0
while index != len(given_list):
   print(f'type of {given_list[index]} = {type(given_list[index])}')
   if index == len(given_list):
       break
   index += 1

print('\nTask 4\n')

list_1 = [2,46,8,4,6]
max_number = max(list_1)
print(f'max number of list_1 = {max_number}')
min_number = min(list_1)
print(f'min number of list_1 = {min_number}')

list_2 = [3,4,6,89,0]
max_number = max(list_2)
print(f'max number of list_2 = {max_number}')
min_number = min(list_2)
print(f'min number of list_2 = {min_number}')

simmilar_elements = list(set(list_1) & set(list_2))
print(simmilar_elements)
