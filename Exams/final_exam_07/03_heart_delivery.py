neighborhood = list(map(int, input().split("@")))
house = 0

while True:
    command = input().split(" ")

    if command[0] == "Love!":
        break

    elif command[0] == "Jump":
        jump_value = int(command[1])
        house += jump_value

        if house >= len(neighborhood):
            house = 0

        if neighborhood[house] != 0:
            neighborhood[house] -= 2
            if neighborhood[house] == 0:
                print(f"Place {house} has Valentine's day.")

        else:
            print(f"Place {house} already had Valentine's day.")

print(f"Cupid's last position was {house}.")

if sum(neighborhood) == 0:
    print(f"Mission was successful.")

else:
    house_count = 0
    for i in neighborhood:
        if i != 0:
            house_count += 1

    print(f"Cupid has failed {house_count} places.")
