energy = 100
energy_gained = 0
coins = 100
working_day_events = input().split("|")
flag = False

for x in range(len(working_day_events)):

    x_list = working_day_events[x].split("-")
    element_1_x = x_list[0]
    element_2_x = x_list[1]

    if element_1_x == "rest":
        energy_gained = 0
        energy_gained += int(element_2_x)
        if (energy + energy_gained) > 100:
            energy_gained = 100 - energy
            energy += energy_gained
            print(f"You gained {energy_gained} energy.")
            print(f"Current energy: {energy}.")
        elif (energy + energy_gained) <= 100:
            energy += energy_gained
            print(f"You gained {energy_gained} energy.")
            print(f"Current energy: {energy}.")

    if element_1_x == "order":
        if (energy - 30) >= 0:
            energy -= 30
            coins += int(element_2_x)
            print(f"You earned {int(element_2_x)} coins.")
        elif (energy - 30) < 0:
            energy += 50
            print("You had to rest!")

    if element_1_x != "rest" and element_1_x != "order":
        coin_loss = int(element_2_x)
        if (coins - coin_loss) >= 0:
            coins -= coin_loss
            print(f"You bought {element_1_x}.")
        elif (coins - coin_loss) < 0:
            coins -= coin_loss
            print(f"Closed! Cannot afford {element_1_x}.")
            flag = True
            break
if not flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
