circle = input().split(" ")
step = int(input())
killed = []
counter = 0
index = 0

while len(circle) > 0:
    counter += 1

    if counter % step == 0:
        killed.append(circle.pop(index))

    else:
        index += 1

    if index >= len(circle):
        index = 0

killed = [int(i) for i in killed]
print(str(killed).replace(' ', ''))
