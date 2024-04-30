def ascii_sumator(start, finish, sequence):

    sumator = 0

    for symbol in sequence:
        if ord(symbol) in range(ord(start) + 1, (ord(finish))):
            sumator += ord(symbol)

    return sumator


a = input()
b = input()
c = input()

print(ascii_sumator(a, b, c))
