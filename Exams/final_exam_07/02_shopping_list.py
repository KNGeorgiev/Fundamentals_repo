initial_list = input().split("!")

while True:
    command = input().split(" ")

    if command[0] == "Go" and command[1] == "Shopping!":
        break

    elif command[0] == "Urgent":
        if command[1] not in initial_list:
            initial_list.insert(0, command[1])

    elif command[0] == "Unnecessary":
        if command[1] in initial_list:
            initial_list.remove(command[1])

    elif command[0] == "Correct":
        if command[1] in initial_list:
            old_item_idx = initial_list.index(command[1])
            initial_list[old_item_idx] = command[2]

    elif command[0] == "Rearrange":
        if command[1] in initial_list:
            initial_list.remove(command[1])
            initial_list.append(command[1])

print(", ".join(initial_list))
