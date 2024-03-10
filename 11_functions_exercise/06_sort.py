sequence = input().split(' ')
int_sequence = []

for i in sequence:
    int_sequence.append(int(i))

sorted_list = sorted(int_sequence)
print(sorted_list)
