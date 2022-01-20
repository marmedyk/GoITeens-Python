#Завдання #1
print('\ntask #1\n')


x = '10'
y = '5'
z = '20'
print(int(x) == int(y))
print(int(x) >= int(y))
print(int(x) <= int(y))
print(int(x) > int(y))
print(int(x) < int(y))
print(int(x) != int(y))
print(int(z) == int(y))
print(int(z) >= int(y))
print(int(z) <= int(y))
print(int(z) > int(y))
print(int(z) < int(y))
print(int(z) != int(y))
print(int(x) == int(z))
print(int(x) >= int(z))
print(int(x) <= int(z))
print(int(x) > int(z))
print(int(x) < int(z))
print(int(x) != int(z))


#Завдання #2
print('\ntask #2\n')


given_string = '    i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone   '

print(len(given_string))
print(given_string[4:-3])
print(given_string.count('a'))
print(given_string.upper())
print(given_string.lower())
print(given_string.replace('super power', 'tasty breakfast'))
print(given_string.isalpha())
new_given_string = given_string.replace(' ', '-')
print(new_given_string.replace('i','1'))


#Завдання #3
print('\ntask #3\n')


Name = input('Type your name(Ex. Ivan): ')
Surname = input(f'Hello {Name}, type your surname(Ex. Lizun): ')
Fathername = input(f"Hello {Surname} {Name}, type your father's name(Ex. Oleksa): ")
Birthdate = input(f"Hello {Surname} {Name} whose father's name is {Fathername}, type your birthdate(Ex. 12.04.1992) ")
print(f'''
SNF = {Surname[0]}{Name[0]}{Fathername[0]}
Surname = {Surname}
Name = {Name}
Father's name = {Fathername}
Birthdate = {Birthdate}
''')
