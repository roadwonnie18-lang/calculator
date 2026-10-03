import math
import time
bot_name: str = 'big daddy'
print(f'Hi I am {bot_name} what do you want')

while True:
    user_input: str = input('You:').lower()

    if user_input in ['hi', 'hello']:
        print(f'{bot_name}: HI, what do you want')

    elif user_input in ['bye', 'goodbye']:
        print(f'{bot_name}: BYE')
        time.sleep(3)
        break

    elif user_input in ['+', 'add']:
        print(f'{bot_name}: what do you want to add?')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            third_input = input('Third number: (or just press enter)').strip.()
            if third_input in ['', 'none', 'null', 'no number']:
                num3 = 0.0
            else:
                num3 = float(third_input)
                
            print(f'{bot_name}: The sum is {num1 + num2 + num3}')
        except ValueError:
            print(f'{bot_name}: Please enter a valid number')

    elif user_input in ['-', 'subtract']:
        print(f'{bot_name}: what do you want to subtract?')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            third_input = input('Third number: (or just press enter)')
            if third_input in ['', 'none', 'null', 'no number']:
                num3 = 0.0
            else:
                num3 = float(third_input)     
            print(f'{bot_name}: The difference is {num1 - num2 - num3}')
        except ValueError:
            print(f'{bot_name}: Please enter a valid number')

    elif user_input in ['x', '*', 'multiply']:
        print(f'{bot_name}: what do you want to multiply?')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: ')) 
            third_input = input('Third number: (or just press enter)')
            if third_input in ['', 'none', 'null', 'no number']:
                num3 = 1.0
            else:
                num3 = float(third_input)
            print(f'{bot_name}: The product is {num1 * num2}')
        except ValueError:
            print(f'{bot_name}: Please enter a valid number')

    elif user_input in ['/', 'divide']:
        print(f'{bot_name}: what do you want to divide?')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            third_input = input('Third number: (or just press enter)')
            if third_input in ['', 'none', 'null', 'no number']:
                num3 = 1.0
            else:
                num3 = float(third_input)
            print(f'{bot_name}: The quotient is {num1 / num2}')
        except ValueError:
            print(f'{bot_name}: Please enter a valid number')
        except ZeroDivisionError:
            print(f'{bot_name}: W-w what have you done you broke it what did you expect?')
            time.sleep(2)
            print(f'{bot_name}: you killed me i hope it was worth it')
            time.sleep(5)
            break

    elif user_input in ['**', 'exponent', 'exponents']:
        num1: float = float(input('Base number: '))
        num2: float = float(input('Exponent number: '))
        print(f'{bot_name}: The product is {num1 ** num2}')

    elif user_input in ['square root', 'sqrt']:
        print(f'{bot_name}: what do you want to find the square root of?')
        num1: float = float(input('Number:'))
        print(f'{bot_name}: The square root is {math.sqrt(num1)}')

    elif user_input in ['cube root', 'cubed root']:
        print(f'{bot_name}: what do you want to find the cubed root of?')
        num1: float = float(input('Number:'))
        print(f'{bot_name}: The cubed root is {math.cbrt(num1)}')


    elif user_input in ['/help', 'help']:
        print(f'{bot_name}: you can say add, subtract, multiply or divide it is just a simple calculator')

    else:
        print(f'{bot_name}: Please enter a valid command')


