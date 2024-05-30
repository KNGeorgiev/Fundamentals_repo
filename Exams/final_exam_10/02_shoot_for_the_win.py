sequence = list(map(int, input().split(" ")))
shot_targets = 0

while True:

    command = input()

    if command == "End":
        unpacked_sequence = [str(x) for x in sequence]
        print(f"Shot targets: {shot_targets} -> {' '.join(unpacked_sequence)}")
        break

    else:
        shot_index = int(command)
        if shot_index < len(sequence):
            if sequence[shot_index] != -1:
                initial_number = sequence[shot_index]
                shot_targets += 1
                sequence[shot_index] = -1
                for index, others in enumerate(sequence):
                    if others != -1:
                        if others > initial_number:
                            sequence[index] -= initial_number
                        else:
                            sequence[index] += initial_number
