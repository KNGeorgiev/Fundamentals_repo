password = input()

while True:
    command = input().split(" ")

    if command[0] == "Done":
        print(f"Your password is: {password}")
        break

    elif command[0] == "TakeOdd":
        new_password = ""
        for i,s in enumerate(password):
            if i % 2 != 0:
                new_password += s
        password = new_password
        print(password)

    elif command[0] == "Cut":
        idx = int(command[1])
        leng = int(command[2])
        password = password[:idx] + password[idx + leng:]
        print(password)

    elif command[0] == "Substitute":
        old = command[1]
        new = command[2]
        if old in password:
            password = password.replace(old, new)
            print(password)
        else:
            print("Nothing to replace!")
