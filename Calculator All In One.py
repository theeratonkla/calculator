import math

Program = input('''
Please select the type of program you want to perform:
1 for addition, subtraction, multiplication, division, exponentiation and root
2 for factorial, absolute value, 1/number, percentage, round up and round down
3 for change base number
4 for check your BMI
5 for trigonometry
''')

if Program == '1':
    exec(open("CalculatorAllInOne 1.py").read())
elif Program == '2':
    exec(open("CalculatorAllInOne 2.py").read())
elif Program == '3':
    exec(open("CalculatorAllInOne 3.py").read())
elif Program == '4':
    exec(open("CalculatorAllInOne 4.py").read())
elif Program == '5':
    exec(open("CalculatorAllInOne 5.py").read())
else:
    print('Enter a valid operator, please run the program again.')

x = input('''
Please select Do you want to continue or end:
1 for continue
0 for end
 ''')

while x == '1':
    Program = input('''
Please select the type of program you want to perform:
1 for addition,subtraction,multiplication,division,exponentiation and root
2 for factorial,absolute value and 1/number
3 for change base number
4 for check your BMI
5 for trigonometry
''')

    if Program == '1':
        exec(open("CalculatorAllInOne 1.py").read())
    elif Program == '2':
        exec(open("CalculatorAllInOne 2.py").read())
    elif Program == '3':
        exec(open("CalculatorAllInOne 3.py").read())
    elif Program == '4':
        exec(open("CalculatorAllInOne 4.py").read())
    elif Program == '5':
        exec(open("CalculatorAllInOne 5.py").read())
    else:
        print('Enter a valid operator, please run the program again.')

    x = input('''
Please select Do you want to continue or end:
1 for continue
0 for end
''')
