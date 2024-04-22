force_users = {}

while True:

    command = input()

    if command == "Lumpawaroo":
        break

    elif " | " in command:
        command = command.split(" | ")
        f_side = command[0]
        f_user = command[1]
        present_in_list = False
        for value in force_users.values():
            if f_user in value:
                present_in_list = True
                break

        if not present_in_list:
            if f_side not in force_users.keys():
                force_users[f_side] = [f_user]
            else:
                force_users[f_side].append(f_user)

    elif " -> " in command:
        command = command.split(" -> ")
        f_user = command[0]
        f_side = command[1]
        for key, value in force_users.items():
            if f_user in value:
                force_users[key].remove(f_user)

        if f_side not in force_users.keys():
            force_users[f_side] = [f_user]
            print(f"{f_user} joins the {f_side} side!")
        else:
            force_users[f_side].append(f_user)
            print(f"{f_user} joins the {f_side} side!")

for key, value in force_users.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for member in value:
            print(f"! {member}")
