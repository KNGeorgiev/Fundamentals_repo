sequence = input().split()
result = 0

for combination in sequence:

    combination = combination.strip()
    num = int(combination[1: -1])

    if combination[0].isupper():
        alphabet_position = ord(combination[0]) - 64
        result += num / alphabet_position

    else:
        alphabet_position = ord(combination[0]) - 96
        result += num * alphabet_position

    if combination[-1].isupper():
        alphabet_position = ord(combination[-1]) - 64
        result -= alphabet_position

    else:
        alphabet_position = ord(combination[-1]) - 96
        result += alphabet_position

print(f"{result:.2f}")
