

while True:
        YES = ['+', 'yes', 'YES', 'так', 'ТАК', 'Yes', 'YES!', 'Yes!', 'yes!', 'так!', 'Так!', 'ТАК!', 'Так', 'y', 'Y']
        NO = ['-', 'no', 'NO', 'ні', 'НІ', 'No', 'NO!', 'No!', 'no!', 'ні!', 'Ні!', 'НІ!', 'Ні', 'n', 'N']
        operations = ['+', 'додавання', '-', 'віднімання', '*', '/', '**', 'множення', 'ділення', 'степінь']
# ПЕРШЕ ЧИСЛО

        while True:
            first_number = input('Введіть перше число: ')
            if first_number.isdigit() is True:
                print(f'Ваше перше число: {first_number}')
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

            second_number = input('Введіть друге число: ')
            if second_number.isdigit() is True:
                print(f'Ваше друге число: {second_number}')
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

        while True:

            # while True:
            #
            #     second_number = input('Введіть друге число: ')
            #     if second_number.isdigit() is True:
            #         print(f'Ваше друге число: {second_number}')
            #         break
            #
            #     else:
            #         while True:
            #             print('На жаль, ми не можемо розпізнати ваш варіант, введіть, будь ласка, ще раз')
            #             again0 = input(f'''\nСпробувати ще раз?\n\n(Можливі варіанти відповідей:\n{YES}\n{NO})\n\n''')
            #
            #             if again0 in NO:
            #                 exit('Гаразд. Програма деактивована')
            #             elif again0 in YES:
            #                 break
            #             else:
            #                 continue


            print('''\nСписок операцій(в дужках вказані альтернативні назви):\n+(додавання)\n-(віднімання)\n*(множення)\n/(ділення)\n**(степінь)\n                ''')
            operation = input('Введіть операцію: ')

            if operation == '+' or operation == 'додавання':
                print(f'{first_number} + {second_number} = {int(first_number) + int(second_number)}')
                break

            elif operation == '-' or operation == 'віднімання':
                print(f'{first_number} - {second_number} = {int(first_number) - int(second_number)}')
                break

            elif operation == '*' or operation == 'множення':
                print(f'{first_number} * {second_number} = {int(first_number) * int(second_number)}')
                break

            elif  second_number== '0' and operation == '/' or second_number == '0' and operation == 'ділення':

                again0 = input(f'''\nна 0 ділити не можна. Ввести іншу операцію?\n\n(можливі варіанти відповідей:\n{YES}\n{NO})\n\n''')

                if again0 in NO:
                    print('Гаразд. Програма деактивована')
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
            elif operation == '/' or operation == 'ділення':
                print(f'{first_number} / {second_number} = {int(first_number) / int(second_number)}')
                break
            elif operation == '**' or operation == 'степінь':
                print(f'{first_number} ** {second_number} = {int(first_number) ** int(second_number)}')
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


