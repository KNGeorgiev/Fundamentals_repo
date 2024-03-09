x = input()
y = input()


def symbol_borders(a, b):
    a = ord(a)
    b = ord(b)

    for num in range(a + 1, b):
        print(chr(num), end=' ')


symbol_borders(x, y)
