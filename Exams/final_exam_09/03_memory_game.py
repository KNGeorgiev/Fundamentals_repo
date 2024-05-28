sequence = input().split(" ")
counter = 0

while True:
    command = input().split(" ")
    counter += 1

    if command[0] == "end":
        print(f"Sorry you lose :(")
        print(*sequence)
        break

    else:
        index_1 = int(command[0])
        index_2 = int(command[1])
        if index_1 == index_2 or index_1 < 0 or index_2 < 0 or index_1 >= len(sequence) or index_2 >= len(sequence):
            mid = int((len(sequence) / 2))
            sequence.insert(mid, "-" + (str(counter) + "a"))
            sequence.insert(mid + 1, "-" + (str(counter) + "a"))
            print("Invalid input! Adding additional elements to the board")

        elif sequence[index_1] == sequence[index_2]:
            print(f"Congrats! You have found matching elements - {sequence[index_1]}!")
            if index_1 > index_2:
                sequence.pop(index_1)
                sequence.pop(index_2)
            elif index_1 < index_2:
                sequence.pop(index_2)
                sequence.pop(index_1)

        elif sequence[index_1] != sequence[index_2]:
            print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {counter} turns!")
        break
