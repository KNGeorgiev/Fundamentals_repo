wagon_number = int(input())
wagon_list = [0 for num in range(wagon_number)]


while True:
    command = input().split(' ')

    if command[0] == 'End':
        break

    elif command[0] == 'add':
        wagon_list[wagon_number - 1] = wagon_list[wagon_number - 1] + int(command[1])

    elif command[0] == 'insert':
        wagon_list[int(command[1])] = wagon_list[int(command[1])] + int(command[2])

    elif command[0] == 'leave':
        wagon_list[int(command[1])] = wagon_list[int(command[1])] - int(command[2])


print(wagon_list)
