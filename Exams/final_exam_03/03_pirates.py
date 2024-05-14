cities_dict = {}

while True:
    command = input()

    if command == "Sail":
        break

    else:
        city, population, gold = command.split("||")
        population = int(population)
        gold = int(gold)
        if city not in cities_dict.keys():
            cities_dict[city] = {"population": population, "gold": gold}
        else:
            cities_dict[city]["population"] += population
            cities_dict[city]["gold"] += gold

while True:
    action = input().split("=>")

    if action[0] == "End":
        if cities_dict:
            print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
            for key in cities_dict.keys():
                print(f"{key} -> Population: {cities_dict[key]['population']} citizens, "
                      f"Gold: {cities_dict[key]['gold']} kg")
        else:
            print("Ahoy, Captain! All targets have been plundered and destroyed!")
        break

    elif action[0] == "Plunder":
        town = action[1]
        ppl = int(action[2])
        money = int(action[3])
        cities_dict[town]["population"] -= ppl
        cities_dict[town]["gold"] -= money
        print(f"{town} plundered! {money} gold stolen, {ppl} citizens killed.")
        if cities_dict[town]["population"] <= 0 or cities_dict[town]["gold"] <= 0:
            del cities_dict[town]
            print(f"{town} has been wiped off the map!")

    elif action[0] == "Prosper":
        town = action[1]
        money = int(action[2])
        if money < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities_dict[town]["gold"] += money
            print(f"{money} gold added to the city treasury. {town} now has {cities_dict[town]['gold']} gold.")
