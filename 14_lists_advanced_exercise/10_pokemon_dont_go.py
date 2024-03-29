sequence = [int(i) for i in input().split()]
pokemon_counter = 0

while len(sequence) > 0:

    idx = int(input())

    if idx >= len(sequence):
        current = sequence[-1]
        pokemon_counter += sequence[-1]
        sequence[-1] = sequence[0]

    elif idx < 0:
        current = sequence[0]
        pokemon_counter += sequence[0]
        sequence[0] = sequence[-1]

    else:
        current = sequence[idx]
        pokemon_counter += sequence[idx]
        sequence.pop(idx)

    sequence = [x + current if x <= current else x - current for x in sequence]

print(pokemon_counter)
