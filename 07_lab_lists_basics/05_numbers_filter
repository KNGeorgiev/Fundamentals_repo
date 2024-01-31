n = int(input())
num_list = []
filtered = []

for x in range(n):
    current_number = int(input())
    num_list.append(current_number)

command = input()

if command == "even":
    for number in num_list:
        if number % 2 == 0:
            filtered.append(number)

if command == "odd":
    for number in num_list:
        if number % 2 != 0:
            filtered.append(number)

if command == "negative":
    for number in num_list:
        if number < 0:
            filtered.append(number)

if command == "positive":
    for number in num_list:
        if number >= 0:
            filtered.append(number)

print(filtered)
