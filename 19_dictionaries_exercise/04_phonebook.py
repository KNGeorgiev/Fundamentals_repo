phonebook = {}
n = 0

while True:

    data = input()

    if "-" not in data:
        n = int(data)
        break

    else:
        data = data.split("-")
        name = data[0]
        number = data[1]
        phonebook[name] = number

for x in range(n):
    check = input()

    if check not in phonebook:
        print(f"Contact {check} does not exist.")
    else:
        print(f"{check} -> {phonebook[check]}")
