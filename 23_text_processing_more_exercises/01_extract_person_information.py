n = int(input())

for i in range(n):
    info = input()
    name = ""
    age = ""

    for index, symbol in enumerate(info):
        if symbol == "@":
            start_n = index + 1

        if symbol == "#":
            start_a = index + 1

        if symbol == "|":
            name = info[start_n: index]

        if symbol == "*":
            age = info[start_a: index]

    print(f"{name} is {age} years old.")
