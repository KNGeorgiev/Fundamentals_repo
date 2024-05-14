raw_activation_key = input()

while True:
    command= input().split(">>>")

    if command[0] == "Generate":
        print(f"Your activation key is: {raw_activation_key}")
        break

    elif command[0] == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        command_type = command[1]
        start = int(command[2])
        finish = int(command[3])
        if command_type == "Upper":
            raw_activation_key = raw_activation_key[: start] + raw_activation_key[start:finish].upper() + raw_activation_key[finish:]
        elif command_type == "Lower":
            raw_activation_key = raw_activation_key[: start] + raw_activation_key[start:finish].lower() + raw_activation_key[finish:]
        print(raw_activation_key)

    elif command[0] == "Slice":
        start = int(command[1])
        finish = int(command[2])
        raw_activation_key = raw_activation_key[: start] + raw_activation_key[finish:]
        print(raw_activation_key)
