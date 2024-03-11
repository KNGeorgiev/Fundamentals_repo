sequence = input().split(' ')
int_sequence = []

for i in sequence:
    int_sequence.append(int(i))

min_num = min(int_sequence)
max_num = max(int_sequence)
sum_num = sum(int_sequence)

print(f'The minimum number is {min_num}')
print(f'The maximum number is {max_num}')
print(f'The sum number is: {sum_num}')
