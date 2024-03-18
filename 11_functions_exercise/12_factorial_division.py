from math import factorial


def factorial_division(a, b):

    x = factorial(a)
    y = factorial(b)

    return print(f'{x / y:.2f}')


num1 = int(input())
num2 = int(input())
factorial_division(num1, num2)
