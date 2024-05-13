line_num = int(input())
plant_dict = {}

for x in range(line_num):
    plant_rarity_info = input().split("<->")
    plant = plant_rarity_info[0]
    rarity = plant_rarity_info[1]
    plant_dict[plant] = {"rarity": int(rarity), "rating": []}

while True:
    command = input().split(": ")

    if command[0] == "Exhibition":
        print("Plants for the exhibition:")
        for plant in plant_dict.keys():
            if len(plant_dict[plant]['rating']) > 0:
                average_rating = sum(plant_dict[plant]['rating']) / len(plant_dict[plant]['rating'])
            else:
                average_rating = 0
            print(f"- {plant}; Rarity: {plant_dict[plant]['rarity']}; Rating: {average_rating:.2f}")
        break

    elif command[0] == "Rate":
        rate_data = command[1].split(" ")
        rate_plant = rate_data[0]
        rating = int(rate_data[2])
        if rate_plant in plant_dict:
            plant_dict[rate_plant]["rating"].append(rating)
        else:
            print("error")

    elif command[0] == "Update":
        update_data = command[1].split(" ")
        update_plant = update_data[0]
        update_rarity = int(update_data[2])
        if update_plant in plant_dict:
            plant_dict[update_plant]["rarity"] = update_rarity
        else:
            print("error")

    elif command[0] == "Reset":
        reset_plant = command[1]
        if reset_plant in plant_dict:
            plant_dict[reset_plant]["rating"].clear()
        else:
            print("error")
