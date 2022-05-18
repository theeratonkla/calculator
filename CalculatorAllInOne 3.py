import math

past = int(input('''
Please select the type of base number you want to change from:
 '''))
future = int(input('''
Please select the type of base number you want to change to:
2 for Binary
8 for Octal
10 for Decimal
16 for Hexademical
 '''))

num_1 = input('Enter your number: ')
num_2 = int(num_1, past)

if future == 2:
    num_2 = bin(num_2)
    print('{} in base number {} is {} in binary'.format(num_1, past, num_2))

elif future == 8:
    num_2 = oct(num_2)
    print('{} in base number {} is {} in octal'.format(num_1, past, num_2))

elif future == 10:
    print('{} in base number {} is {} in decimal'.format(num_1, past, num_2))

elif future == 16:
    num_2 = hex(num_2)
    print('{} in base number {} is {} in hexadecimal'.format(num_1, past, num_2))

else:
    print('Enter a valid operator, please run the program again.')
