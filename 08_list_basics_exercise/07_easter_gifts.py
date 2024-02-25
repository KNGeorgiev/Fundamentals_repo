gifts = input().split(" ")
command = input()

while "No Money" not in command:

    if "OutOfStock" in command:
        command = command.split(" ")
        none_gift = command[1]
        for i in range(len(gifts)):
            if gifts[i] == none_gift:
                gifts[i] = "None"

    elif "Required" in command:
        command = command.split(" ")
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]

    elif "JustInCase" in command:
        command = command.split(" ")
        gifts[-1] = command[1]

    command = input()

final = []

for i in range(len(gifts)):
    if gifts[i] != "None":
        final.append(gifts[i])

final_as_string = " ".join([str(i) for i in final])

print(final_as_string)
