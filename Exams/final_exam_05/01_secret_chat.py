concealed_message = input()

while True:
    command = input().split(":|:")

    if command[0] == "Reveal":
        print(f"You have a new text message: {concealed_message}")
        break

    elif command[0] == "InsertSpace":
        idx = int(command[1])
        concealed_message = concealed_message[:idx] + " " + concealed_message[idx:]
        print(concealed_message)

    elif command[0] == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            start_idx = concealed_message.find(substring)
            final_idx = start_idx + len(substring)
            concealed_message = concealed_message[:start_idx] + substring[::-1] + concealed_message[final_idx:]
            print(concealed_message)
        else:
            print("error")

    elif command[0] == "ChangeAll":
        old = command[1]
        new = command[2]
        while old in concealed_message:
            concealed_message = concealed_message.replace(old, new)
        print(concealed_message)
