def data_types(a, b):

    if a == 'int':
        print(int(b) * 2)

    elif a == 'real':
        print(f'{float(b) * 1.5:.2f}')

    elif a == 'string':
        print(f'${b}$')


x = input()
y = input()
data_types(x, y)
