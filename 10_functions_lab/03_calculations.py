op = input()
num1 = int(input())
num2 = int(input())


def my_calculator(operator, a, b):

    if operator == 'multiply':
        return int(a * b)
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return int(a + b)
    elif operator == 'subtract':
        return int(a - b)


print(my_calculator(op, num1, num2))
