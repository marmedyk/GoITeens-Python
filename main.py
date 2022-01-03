print("Hello world!")
hello = 1
print(hello)


x=3
messege = "123456789"
print(messege[::-x])

#урок 2 дз
print('')
print('урок 2 дз')

#завдання #1
OH = '''
#########
#     #
#     #
#     #
#########

#     #
#     #
#########
#     #
#     #'''
print(OH)


#завдання #2
Song = "\n\nперший спосіб\nWe all live in a yellow submarine\nYellow submarine, yellow submarine\nWe all live in a yellow submarine\nYellow submarine, yellow submarine\n\nWe all live in a yellow submarine\nYellow submarine, yellow submarine\nWe all live in a yellow submarine\nYellow submarine, yellow submarine\n\n"
print(Song)

Song1 = '''
We all live in a yellow submarine
Yellow submarine, yellow submarine
We all live in a yellow submarine
Yellow submarine, yellow submarine

We all live in a yellow submarine
Yellow submarine, yellow submarine
We all live in a yellow submarine
Yellow submarine, yellow submarine

'''
print("другий спосіб"+Song1)

Song2 = '''
We all live in a yellow submarine
Yellow submarine, yellow submarine
We all live in a yellow submarine
Yellow submarine, yellow submarine
'''
print("третій спосіб"+2*Song2)


#завдання #3
print('What\'s your name?')

name = input()
print('And surname')
surname = input()
print('I am Groot!')
print('I am Steve Rogers!')
print('I am', name, surname + '!')

#завдання #3 варіант 2
name='Marko'
surname='Medyk'
print('''
спосіб 2(без приколів)''')
print('I am Groot!')
print('I am Steve Rogers!')
print('I am', name, surname + '!')

#завдання #4
start_string = "abcdefghijklmn"
new_string_first = start_string[0:4]
new_string_reverse_var1 = start_string[9:14]
new_string_prereverse = start_string[-1:-6:-1]
new_string_reverse_var2 = new_string_prereverse[::-1]
new_string_mid = start_string[5:-5]
every_second = start_string[1::2]
print('')
print('')
print(new_string_first)
print(new_string_reverse_var1)
print(new_string_reverse_var2)
print(new_string_mid)
print(every_second)

#завдання #5
x=5
y=2
π=3.14159265358979323846
π1=(round(π, 4))
print('')
print('')
print(f'Sum {x} + {y} = {x+y}')
print(f'Difference {x} - {y} = {x-y}')
print(f'Product {x} * {y} = {x*y}')
print(f'Quotient {x} / {y} = {x/y}')
print(f'{x} to the power of {y} = {x**y}')
print(f'You can divide {x} by {y} without modulo for {x//y} times')
print(f'Modulo {x} % {y} = {x%y}')
print('π = ', π1)








