import math

choice = input('''
Please select the type of operation you want to perform:
! for factorial
|| for absolute value
1/ for 1/number
% for percentage
ceil for round up
floor for round down
''')

num = float(input('Enter your number: '))

if choice == '!':
    print('{} ! = '.format(num))
    print(math.factorial(num))

elif choice == '||':
    print('|{}|  = '.format(num))
    print(abs(num))

elif choice == '1/':
    print('1/{}  = '.format(num))
    print(1 / num)

elif choice == '%':
    print('{}% = '.format(num))
    print(num/100)

elif choice == 'ceil':
    print('round up of {}  = '.format(num))
    print(math.ceil(num))

elif choice == 'floor':
    print('round down of {}  = '.format(num))
    print(math.floor(num))

else:
    print('Enter a valid operator, please run the program again.')
