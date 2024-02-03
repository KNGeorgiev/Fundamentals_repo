string = input().split(" ")
shuffle = int(input())

lenght = len(string)
half = int(lenght / 2)

for i in range(0, shuffle):
    final = []
    for y in range(0, half):
        final.append(string[y])
        final.append(string[half])
        half += 1

    string = final
    half = int(lenght / 2)

print(string)
