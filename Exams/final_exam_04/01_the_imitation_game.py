encrypted_message = input()

while True:
    command = input()

    if command == "Decode":
        break

    else:
        command = command.split("|")

        if "Move" == command[0]:
            letter_num = int(command[1])
            first = encrypted_message[:letter_num]
            second = encrypted_message[letter_num:]
            encrypted_message = second + first

        elif "Insert" == command[0]:
            idx = int(command[1])
            vlu = command[2]
            encrypted_message = list(encrypted_message)
            encrypted_message.insert(idx, vlu)
            encrypted_message = "".join(encrypted_message)

        elif "ChangeAll" == command[0]:
            substr = command[1]
            replacement = command[2]
            while substr in encrypted_message:
                encrypted_message = encrypted_message.replace(substr, replacement)

print(f"The decrypted message is: {encrypted_message}")
