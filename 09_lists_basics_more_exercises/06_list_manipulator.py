sequence = input().split(' ')
int_sequence = []
even_list = []
odd_list = []
first_count_list = []
last_count_list = []

for element in sequence:
    int_sequence.append(int(element))

while True:

    command = input().split(' ')

    if command[0] == 'end':
        print(int_sequence)
        break

    elif command[0] == 'exchange':
        if int(command[1]) >= len(int_sequence) or int(command[1]) < 0:
            print('Invalid index')
        else:
            first_part = int_sequence[int(command[1]) + 1:]
            second_part = int_sequence[0:int(command[1]) + 1]
            int_sequence = first_part + second_part

    elif command[0] == 'max':
        if command[1] == 'even':
            for num in int_sequence:
                if num % 2 == 0:
                    even_list.append(num)
            if len(even_list) == 0:
                print('No matches')
            else:
                print((len(int_sequence) - 1) - int_sequence[::-1].index(max(even_list)))
            even_list = []

        elif command[1] == 'odd':
            for num in int_sequence:
                if num % 2 != 0:
                    odd_list.append(num)
            if len(odd_list) == 0:
                print('No matches')
            else:
                print((len(int_sequence) - 1) - int_sequence[::-1].index(max(odd_list)))
            odd_list = []

    elif command[0] == 'min':
        if command[1] == 'even':
            for num in int_sequence:
                if num % 2 == 0:
                    even_list.append(num)
            if len(even_list) == 0:
                print('No matches')
            else:
                print((len(int_sequence) - 1) - int_sequence[::-1].index(min(even_list)))
            even_list = []

        elif command[1] == 'odd':
            for num in int_sequence:
                if num % 2 != 0:
                    odd_list.append(num)
            if len(odd_list) == 0:
                print('No matches')
            else:
                print((len(int_sequence) - 1) - int_sequence[::-1].index(min(odd_list)))
            odd_list = []

    elif command[0] == 'first':
        if int(command[1]) > len(int_sequence):
            print("Invalid count")

        elif command[2] == 'even':
            for num in int_sequence:
                if num % 2 == 0:
                    first_count_list.append(num)
                    if len(first_count_list) == int(command[1]):
                        break
            print(first_count_list)
            first_count_list = []

        elif command[2] == "odd":
            for num in int_sequence:
                if num % 2 != 0:
                    first_count_list.append(num)
                    if len(first_count_list) == int(command[1]):
                        break
            print(first_count_list)
            first_count_list = []

    elif command[0] == "last":
        if int(command[1]) > len(int_sequence):
            print("Invalid count")

        elif command[2] == "even":
            for num in reversed(int_sequence):
                if num % 2 == 0:
                    last_count_list.append(num)
                    if len(last_count_list) == int(command[1]):
                        break
            print(list(reversed(last_count_list)))
            last_count_list = []

        elif command[2] == "odd":
            for num in reversed(int_sequence):
                if num % 2 != 0:
                    last_count_list.append(num)
                    if len(last_count_list) == int(command[1]):
                        break
            print(list(reversed(last_count_list)))
            last_count_list = []
