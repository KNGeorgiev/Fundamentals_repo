sequence = input()
result = ""
explosion_str = 0

for index, symbol in enumerate(sequence):

    if symbol == ">":
        result += symbol
        next_idx = index + 1
        value = sequence[next_idx]
        if value.isdigit():
            explosion_str += int(value)

    else:
        if explosion_str <= 0:
            result += symbol
        else:
            result += ""
            explosion_str -= 1

print(result)
