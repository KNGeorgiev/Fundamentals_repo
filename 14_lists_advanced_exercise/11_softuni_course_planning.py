initial_schedule = input().split(', ')


while True:

    command = input().split(':')

    if command[0] == 'course start':
        break

    elif command[0] == 'Add':
        initial_schedule.append(command[1])

    elif command[0] == 'Insert' and command[1] not in initial_schedule:
        initial_schedule.insert(int(command[2]), command[1])

    elif command[0] == 'Remove':
        initial_schedule.remove(command[1])

        if f'{command[1]}-Exercise' in initial_schedule:
            initial_schedule.remove(f'{command[1]}-Exercise')

    elif command[0] == 'Swap':
        if command[1] and command[2] in initial_schedule:
            swap1_idx = initial_schedule.index(command[1])
            swap2_idx = initial_schedule.index(command[2])
            initial_schedule[swap1_idx], initial_schedule[swap2_idx] = (
                initial_schedule[swap2_idx], initial_schedule[swap1_idx])

        if f'{command[2]}-Exercise' in initial_schedule:
            initial_schedule.remove(f'{command[2]}-Exercise')
            initial_schedule.insert(initial_schedule.index(command[2]) + 1, f'{command[2]}-Exercise')

    elif command[0] == 'Exercise':
        if command[1] in initial_schedule and f'{command[1]}-Exercise' in initial_schedule:
            pass

        elif command[1] in initial_schedule and f'{command[1]}-Exercise' not in initial_schedule:
            lesson_index = initial_schedule.index(command[1])
            initial_schedule.insert((lesson_index + 1), f'{command[1]}-Exercise')

        else:
            initial_schedule.append(command[1])
            initial_schedule.append(f'{command[1]}-Exercise')

counter = 1
for i in initial_schedule:
    print(f'{counter}.{i}')
    counter += 1
