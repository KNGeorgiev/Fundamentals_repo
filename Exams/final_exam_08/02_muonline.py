health = 100
bitcoins = 0
dungeon_rooms = input().split("|")

for index, room in enumerate(dungeon_rooms):

    room = room.split(" ")

    if room[0] == "potion":
        max_health = 100
        potion_power = int(room[1])
        needed_health = max_health - health

        if needed_health >= potion_power:
            health_healed = potion_power
            health += health_healed
        else:
            health_healed = needed_health
            health = 100

        print(f"You healed for {health_healed} hp.")
        print(f"Current health: {health} hp.")

    elif room[0] == "chest":
        money_found = int(room[1])
        bitcoins += money_found
        print(f"You found {money_found} bitcoins.")

    else:
        monster = room[0]
        damage = int(room[1])
        health -= damage

        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {index + 1}")
            break

    if index == len(dungeon_rooms) - 1 and health > 0:
        print(f"You've made it!\n"
              f"Bitcoins: {bitcoins}\n"
              f"Health: {health}")
