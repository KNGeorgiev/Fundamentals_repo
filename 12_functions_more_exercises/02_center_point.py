def center_point(a, b, x, y):
    from math import sqrt
    from math import floor
    c = (a ** 2) + (b ** 2)
    c = sqrt(c)

    z = (x ** 2) + (y ** 2)
    z = sqrt(z)

    if c < z:
        print(f'{floor(a), floor(b)}')
    else:
        print(f'{floor(x), floor(y)}')


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

center_point(num1, num2, num3, num4)
