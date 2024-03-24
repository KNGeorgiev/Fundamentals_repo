sequence1 = input().split(', ')
sequence2 = input().split(', ')
sequence3 = []

for x in sequence1:
    for y in sequence2:
        if x in y:
            if x in sequence3:
                pass
            else:
                sequence3.append(x)

print(sequence3)
