import math

group_size = int(input())
adventure_days = int(input())

coin_chest = 0

for day in range(1, adventure_days + 1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coin_chest += 50
    coin_chest -= (group_size * 2)

    if day % 3 == 0:
        coin_chest -= (group_size * 3)

    if day % 5 == 0:
        coin_chest += (group_size * 20)
        if day % 3 == 0:
            coin_chest -= (group_size * 2)

print(f"{group_size} companions received {math.floor(coin_chest / group_size)} coins each.")
