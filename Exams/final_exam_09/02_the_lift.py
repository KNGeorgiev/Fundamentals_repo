tourist_number = int(input())
lift_wagons = list(map(int, input().split(" ")))


for index, wagon in enumerate(lift_wagons):
    while wagon < 4:
        if tourist_number == 0:
            break
        wagon += 1
        lift_wagons[index] += 1
        tourist_number -= 1


if tourist_number > 0:
    print(f"There isn't enough space! {tourist_number} people in a queue!")
    print(*lift_wagons)
else:
    if len(lift_wagons) * 4 == sum(lift_wagons):
        print(*lift_wagons)
    else:
        print("The lift has empty spots!")
        print(*lift_wagons)
