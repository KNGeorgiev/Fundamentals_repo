number = int(input())

for i in range(1, number + 1):
    print(i * "*")
    if i == number:
        for x in range(number, 0, - 1):
            print((x - 1) * "*")
            
