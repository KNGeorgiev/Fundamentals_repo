def multiplication_sign(a, b, c):

    abc_list = [a, b, c]
    neg_count = len(list(filter(lambda x: (x < 0), abc_list)))

    if 0 in abc_list:
        print('zero')
    elif neg_count % 2 != 0:
        print('negative')
    else:
        print('positive')


num1 = int(input())
num2 = int(input())
num3 = int(input())

multiplication_sign(num1, num2, num3)
