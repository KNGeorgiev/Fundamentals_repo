hero_num = int(input())
hero_dict = {}

for x in range(hero_num):
    hero_name, hp, mp = input().split(" ")
    hero_dict[hero_name] = {"hp": int(hp), "mp": int(mp)}

while True:
    command = input().split(" - ")

    if command[0] == "End":
        for hero in hero_dict:
            print(f"{hero}")
            print(f"  HP: {hero_dict[hero]['hp']}")
            print(f"  MP: {hero_dict[hero]['mp']}")
        break

    elif command[0] == "CastSpell":
        hname = command[1]
        mp_needed = int(command[2])
        sname = command[3]
        if mp_needed <= hero_dict[hname]["mp"]:
            mp_left = hero_dict[hname]["mp"] - mp_needed
            hero_dict[hname]["mp"] -= mp_needed
            print(f"{hname} has successfully cast {sname} and now has {mp_left} MP!")
        else:
            print(f"{hname} does not have enough MP to cast {sname}!")

    elif command[0] == "TakeDamage":
        hname = command[1]
        dmg = int(command[2])
        attacker = command[3]
        hero_dict[hname]["hp"] -= dmg
        if hero_dict[hname]["hp"] > 0:
            print(f"{hname} was hit for {dmg} HP by {attacker} and now has {hero_dict[hname]['hp']} HP left!")
        else:
            print(f"{hname} has been killed by {attacker}!")
            del hero_dict[hname]

    elif command[0] == "Recharge":
        hname = command[1]
        amount = int(command[2])
        mp_diff = 200 - hero_dict[hname]["mp"]
        hero_dict[hname]["mp"] += amount
        if hero_dict[hname]["mp"] > 200:
            hero_dict[hname]["mp"] = 200
            print(f"{hname} recharged for {mp_diff} MP!")
        else:
            print(f"{hname} recharged for {amount} MP!")

    elif command[0] == "Heal":
        hname = command[1]
        amount = int(command[2])
        hp_diff = 100 - hero_dict[hname]["hp"]
        hero_dict[hname]["hp"] += amount
        if hero_dict[hname]["hp"] > 100:
            hero_dict[hname]["hp"] = 100
            print(f"{hname} healed for {hp_diff} HP!")
        else:
            print(f"{hname} healed for {amount} HP!")
