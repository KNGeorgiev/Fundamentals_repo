num1 = int(input())
num2 = int(input())
num3 = int(input())


def comparator(num1, num2, num3):

    comparator_list = []
    comparator_list.append(num1)
    comparator_list.append(num2)
    comparator_list.append(num3)

    return min(comparator_list)


print(comparator(num1, num2, num3))
