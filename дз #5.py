import random

print('\nTask 1\n\n')

#1     створити два списка рандомно згенерованих значень від 0 до 10 по 10 значень в кожному

list1 = []
index = 0
while index < 10:
    list1.append(random.randint(0, 10))
    index += 1
print(f'list1 = {list1}')

list2 = []
index = 0
while index < 10:
    list2.append(random.randint(0, 10))
    index += 1
print(f'list2 = {list2}\n\n')

#1.1   вивести унікальні значення кожного списка

print('Task 1.1\n')
print(f'unique values of list1: {set(list1)}')
print(f'unique values of list2: {set(list2)}\n\n')

#1.2   вивести унікальні значення, які зустрічаються в обох списках

print('Task 1.2\n')
print(f'unique values of list1 and list2: {set(list1+list2)}\n\n')


#2     створити список з десяти рандомно згенерованих значень від 0 до 100

print('Task 2\n')
list0 = random.choices(range(0,101), k = 10)
print(f'10 random choises form 0 to 100: {list0}\n\n')

#2.1   вивести кожне значення через цикл while

print('Task 2.1')
index = 0
print('\nevery value using a cycle "while":')
while index <  len(list0):
    print(list0[index])
    index += 1

#2.2   вивести кожне значення через цикл for

print('\n\nTask 2.2')
print('\nevery value using a cycle "for": ')
for number in list0:
    print(number)

#2.3   створити список з десяти рандомно згенерованих значень від 10 до 100 через list comprehension

print('\n\nTask 2.3')
list0_comprehension = ([random.randint(10, 100) for element in range(0,10)])
print(f'\n10 random choices form 10 to 100 with "list comprehension":\n{list0_comprehension}\n\n')


#3     створити список рандомно згенерованих значень від 20 до 100, які діляться на 2 і 4 без остачі
#3.1   написати цей цикл через while

print('Task 3.1\n')
number_list = []
number = 20
while number < 101:
  if number % 2 == 0 and number % 4 == 0:
      number_list.append(number)
  number += 1

print(f'digits from 20 to 100 which are divided into 2 and 4 without remainder using a cycle "while":\n{number_list}\n\n')

#3.2   через for

print('Task 3.2\n')
number_list = []
for number in range(20,101):
    if number % 2 == 0 and number % 4 == 0:
        number_list.append(number)
    number += 1

print(f'digits from 20 to 100 which are divided into 2 and 4 without remainder using a cycle "for":\n{number_list}\n\n')


#3.3   через list comprehension

print('Task 3.3\n')
random_list =  [number for number in range(20, 101) if number % 2 == 0 and number % 4 == 0]
print(f'digits from 20 to 100 which are divided into 2 and 4 without remainder using "list comprehension":\n{number_list}\n\n')
#4     створити список і вивести кортежі в який міститься індекс і елемент кожного значення зі списку

print('Task 4\n')
listt = random.choices(range(0, 100), k=3)
print(listt)

for tuplee in enumerate(listt):
    print(tuplee)


#5     написати програму, яка б перевіряла введений користувачем пароль на валідність
#     умови наступні:
#         - мінімум 8 символів
#         - велика буква
#         - маленька буква
#         - цифра
#         - символ
print('\n\nTask 5\n')
password = input(f'''Hi!
Password must contain at least 8 symbols, 
including UPPERCASE LETTER, lowercase letter, 
digit123 and special symbols !@#$%^&*( etc.
Enter your password: ''')

min_number = False
upper_letter = False
lower_letter = False
digit = False
special_symbol = False
special_symbols = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '}', '{', ',' ':', '?', '>', '<', '-', '=', '[', ']', ';', ' ', '.', '/',}

if len(password) >= 8:
    min_number = True
else:
    print('Your password contain less than 8 symbols')

if any(element.isupper() for element in password):
    upper_letter = True
else:
    print('Your password doesn\'t contain upper letters')

if any(element.islower() for element in password):
    lower_letter = True
else:
    print('Your password doesn\'t contain lower letters')

if any(element.isdigit() for element in password):
    digit = True
else:
    print('Your password doesn\'t contain digits')

if any(element in special_symbols for element in password):
    special_symbol = True
else:
    print('Your password doesn\'t contain special symbols')

if  min_number and upper_letter and lower_letter and digit and  special_symbol:
    print(f'Your password: {password}')

