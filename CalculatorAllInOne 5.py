import math


choice = input('''
Please select the type of operation you want to perform:
sin for sine (in degree)
cos for cosine (in degree)
tan for tangent (in degree)
asin for arc sine (in degree)
acos for arc cosine (in degree)
atan for arc tangent (in degree)
''')

num_1 = float(input('Enter your number: '))
num = num_1*math.pi/180

if choice == 'sin':
    print('sine of {} is '.format(num_1))
    print(math.sin(num))

elif choice == 'cos':
    print('cosine of {} is '.format(num_1))
    print(math.cos(num))

elif choice == 'tan':
    print('tangent of {} is '.format(num_1))
    print(math.tan(num))

elif choice == 'asin':
    print('arc sine of {} is '.format(num_1))
    print(math.asin(num))

elif choice == 'acos':
    print('arc cosine of {} is '.format(num_1))
    print(math.acos(num))

elif choice == 'atan':
    print('arc tangent of {} is '.format(num_1))
    print(math.atan(num))

else:
    print('Enter a valid operator, please run the program again.')