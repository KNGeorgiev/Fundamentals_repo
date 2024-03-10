sequence = input().split(' ')
int_sequence = []

for i in sequence:
    int_sequence.append(int(i))


def func(x):
    if x % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(func, int_sequence)
print(list(even_numbers))
