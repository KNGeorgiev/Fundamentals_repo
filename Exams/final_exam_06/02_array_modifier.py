collection = list(map(int, input().split(" ")))

while True:

    command = input().split(" ")
    if command[0] == "end":
        break

    elif command[0] == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        collection[index_1], collection[index_2] = collection[index_2], collection[index_1]

    elif command[0] == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        collection[index_1] = collection[index_1] * collection[index_2]

    elif command[0] == "decrease":
        collection = [i - 1 for i in collection]

print(', '.join(map(str, collection)))
