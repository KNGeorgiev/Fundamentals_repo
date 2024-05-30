targets = list(map(int, input().split(" ")))

while True:

    command = input().split(" ")

    if command[0] == "End":
        targets = [str(x) for x in targets]
        print("|".join(targets))
        break

    elif command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])

        if 0 <= index < len(targets):
            if targets[index] - power > 0:
                targets[index] -= power
            else:
                targets.pop(index)

    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])

        if len(targets) > index >= 0:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])

        if 0 <= index - radius and index + radius < len(targets) - 1:
            del targets[index - radius:index + radius * 2]

        else:
            print("Strike missed!")
