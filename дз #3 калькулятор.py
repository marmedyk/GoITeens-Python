a = input('введіть перше число: ')
if a.isdigit() is True:
    print(f'ваше перше число: {a}')
else:
    exit('ви ввели не число, перезапустіть програму')

b = input('введіть друге число: ')
if b.isdigit() is True:
    print(f'ваше друге число: {b}')
else:
    exit('ви ввели не число, перезапустіть програму')

print('''
список операцій(в дужках вказані альтернативні назви):
+(додавання)
-(віднімання)
*(множення)
/(ділення)
**(степінь)
''')
c = input('введіть операцію: ')
if c == '+' or c == 'додавання':
    print(f'{a} + {b} = {int(a) + int(b)}')
elif c == '-' or c == 'віднімання':
    print(f'{a} - {b} = {int(a) - int(b)}')
elif c == '*' or c == 'множення':
    print(f'{a} * {b} = {int(a) * int(b)}')
elif c == '/' or c == 'ділення':
    print(f'{a} / {b} = {int(a) / int(b)}')
elif c == '**' or c == 'степінь':
    print(f'{a} ** {b} = {int(a) ** int(b)}')
else:
    print('на жаль, ми ще не можемо виконати вашу операцію')

