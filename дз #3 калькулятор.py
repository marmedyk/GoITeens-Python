

while True:
        YES = ['+', 'yes', 'YES', 'так', 'ТАК', 'Yes', 'YES!', 'Yes!', 'yes!', 'так!', 'Так!', 'ТАК!', 'Так', 'y', 'Y']
        NO = ['-', 'no', 'NO', 'ні', 'НІ', 'No', 'NO!', 'No!', 'no!', 'ні!', 'Ні!', 'НІ!', 'Ні', 'n', 'N']
        error0 = 0
        operations = ['+', 'додавання', '-', 'віднімання', '*', '/', '**', 'множення', 'ділення', 'степінь']
# ПЕРШЕ ЧИСЛО

        while True:
            a = input('Введіть перше число: ')
            if a.isdigit() is True:
                print(f'Ваше перше число: {a}')
                break
            else:
                while True:
                    print('\nНа жаль, ми не можемо розпізнати ваш варіант, введіть, будь ласка, ще раз')
                    again0 = input(f'''\nСпробувати ще раз?\n\n(Можливі варіанти відповідей:\n{YES}\n{NO})\n\n''')

                    if again0 in NO:
                        exit('Гаразд. Програма деактивована')
                    elif again0 in YES:
                        break
                    else:
                        continue

# ДРУГЕ ЧИСЛО

        while True:

            b = input('Введіть друге число: ')
            if b.isdigit() is True:
                print(f'Ваше друге число: {b}')
                break

            else:
                while True:
                    print('На жаль, ми не можемо розпізнати ваш варіант, введіть, будь ласка, ще раз')
                    again0 = input(f'''\nСпробувати ще раз?\n\n(Можливі варіанти відповідей:\n{YES}\n{NO})\n\n''')

                    if again0 in NO:
                        exit('Гаразд. Програма деактивована')
                    elif again0 in YES:
                        break
                    else:
                        continue

# ОПЕРАЦІЇ і ПОМИЛКА ДІЛЕННЯ НА 0
        error0 = None
        if error0 == None:
            while True:

                print('''\nСписок операцій(в дужках вказані альтернативні назви):\n+(додавання)\n-(віднімання)\n*(множення)\n/(ділення)\n**(степінь)\n                ''')
                c = input('Введіть операцію: ')

                if c == '+' or c == 'додавання':
                    print(f'{a} + {b} = {int(a) + int(b)}')
                    break

                elif c == '-' or c == 'віднімання':
                    print(f'{a} - {b} = {int(a) - int(b)}')
                    break

                elif c == '*' or c == 'множення':
                    print(f'{a} * {b} = {int(a) * int(b)}')
                    break

                elif b == '0' and c == '/' or b == '0' and c == 'ділення':

                    again0 = input(f'''\nна 0 ділити не можна. Ввести інше число?\n\n(можливі варіанти відповідей:\n{YES}\n{NO})\n\n''')

                    if again0 in NO:
                        print('На жаль, программа не може вирішити цю задачу')
                    elif again0 in YES:
                        continue
                    else:
                        while True:
                            print('на жаль ми не можемо розпізнати ваш варіант, введіть, будь ласка ще раз')
                            again0 = input(f'''\nна 0 ділити не можна. Ввести іншу операцію?\n\n(можливі варіанти відповідей:\n{YES}\n{NO})\n\n''')

                            if again0 in NO:
                                exit('Гаразд. Програма деактивована')
                            elif again0 in YES:
                                break
                            else:
                                continue
                elif c == '/' or c == 'ділення':
                    print(f'{a} / {b} = {int(a) / int(b)}')
                    break
                elif c == '**' or c == 'степінь':
                    print(f'{a} ** {b} = {int(a) ** int(b)}')
                    break
                else:
                    while True:
                        print('На жаль, ми не можемо розпізнати ваш варіант, введіть, будь ласка, ще раз')
                        again1 = input(f'''\nСпробувати ще раз?\n\n(Можливі варіанти відповідей:\n{YES}\n{NO})\n\n''')

                        if again1 in NO:
                            exit('Гаразд. Програма деактивована')
                        elif again1 in YES:
                            break
                        else:
                            continue


# ЩЕ РАЗ?

        again = input(f"""\nЩе раз?\n\n(можливі варіанти відповідей:\n{YES}\n{NO})\n\n""")
        if again in NO:
            exit()
        elif again in YES:
            continue
        else:
            while True:
                print('на жаль ми не можемо розпізнати ваш варіант, введіть, будь ласка ще раз')
                again0 = input(f'''\nЩе раз?\n\n(можливі варіанти відповідей:\n{YES}\n{NO})\n\n''')

                if again0 in NO:
                    exit('Гаразд. Програма деактивована')
                elif again0 in YES:
                    break
                else:
                    continue


