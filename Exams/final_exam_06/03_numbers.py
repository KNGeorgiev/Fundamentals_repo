sequence = list(map(int, input().split(" ")))
sequence_average = sum(sequence) / len(sequence)
top_five = []

for x in range(5):
    if max(sequence) > sequence_average:
        top_five.append(max(sequence))
        sequence.remove(max(sequence))

if len(top_five) == 0:
    print("No")

else:
    print(*top_five)
