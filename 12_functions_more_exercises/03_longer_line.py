import math


def longer_line(a, b, c, d, a2, b2, c2, d2):

    line1 = math.sqrt(((c - a)**2) + ((d - b)**2))
    line2 = math.sqrt(((c2 - a2)**2) + ((d2 - b2)**2))

    if line1 >= line2:
        diagonal1 = (a ** 2) + (b ** 2)
        diagonal1 = math.sqrt(diagonal1)
        diagonal2 = (c ** 2) + (d ** 2)
        diagonal2 = math.sqrt(diagonal2)

        if diagonal1 <= diagonal2:
            print(f"{math.floor(a), math.floor(b)}{math.floor(c), math.floor(d)}")

        else:
            print(f"{math.floor(c), math.floor(d)}{math.floor(a), math.floor(b)}")

    else:
        diagonal3 = (a2 ** 2) + (b2 ** 2)
        diagonal3 = math.sqrt(diagonal3)
        diagonal4 = (c2 ** 2) + (d2 ** 2)
        diagonal4 = math.sqrt(diagonal4)

        if diagonal3 <= diagonal4:
            print(f"{math.floor(a2), math.floor(b2)}{math.floor(c2), math.floor(d2)}")

        else:
            print(f"{math.floor(c2), math.floor(d2)}{math.floor(a2), math.floor(b2)}")


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

num5 = float(input())
num6 = float(input())
num7 = float(input())
num8 = float(input())

longer_line(num1, num2, num3, num4, num5, num6, num7, num8)
