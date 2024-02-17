# Simple Calculator
# Create a simple calculator. The calculator should be able to perform basic math operations, add, subtract, divide and multiply. 
# The calculator should take input from users. The calculator should be able to handle ZeroDivisionError, NameError, and ValueError.

def calc():
    try:
        pierwsza = int(input("Podaj pierwszą cyfrę: " ))
        druga = int(input("Podaj drugą: "))
        dzialanie = input("Co robimy? '+' '-' '/' '*' ? ")
        if dzialanie == '+':
            print(pierwsza+druga)
        elif dzialanie == '-':
            print(pierwsza-druga)
        elif dzialanie == '/':
            print(pierwsza-druga)
        elif dzialanie == '*':
            print(pierwsza-druga)
    except ValueError as a:
        print("Zła wartość ", a)
    except ZeroDivisionError as b:
        print("Oj matołku, nie dzielimy przez zero", b)
    except NameError as c:
        print("Programista się nie spisał... x D", c)
    except Exception as d:
        print("A to co ?! ", d)
calc()
