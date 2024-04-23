dragonflights = {}


def dragon_classificator(dragon_data):

    d_type, name, damage, health, armor = dragon_data.split(" ")

    if damage == "null":
        damage = 45

    if health == "null":
        health = 250

    if armor == "null":
        armor = 10

    if d_type not in dragonflights:
        dragonflights[d_type] = {}

    if name not in dragonflights[d_type]:
        dragonflights[d_type][name] = {}

    dragonflights[d_type][name]["damage"] = int(damage)
    dragonflights[d_type][name]["health"] = int(health)
    dragonflights[d_type][name]["armor"] = int(armor)


def result(flights):

    for color in flights:
        dmg, hlth, arm = 0, 0, 0
        dragon_num = len(flights[color])

        for dragon in flights[color]:
            dmg += flights[color][dragon]["damage"]
            hlth += flights[color][dragon]["health"]
            arm += flights[color][dragon]["armor"]

        print(
            f"{color}::"
            f"({dmg / dragon_num:.2f}/"
            f"{(hlth / dragon_num):.2f}/"
            f"{(arm / dragon_num):.2f})"
        )

        for dragonkin in sorted(flights[color].keys()):
            print(
                f"-{dragonkin} -> "
                f"damage: {flights[color][dragonkin]['damage']}, "
                f"health: {flights[color][dragonkin]['health']}, "
                f"armor: {flights[color][dragonkin]['armor']} "
            )


dragon_count = int(input())

for d in range(dragon_count):

    d_info = input()

    dragon_classificator(d_info)

result(dragonflights)
