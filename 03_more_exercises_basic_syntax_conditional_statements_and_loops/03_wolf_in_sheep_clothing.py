animal = input()
animal_list = animal.split(", ")
animal_list.reverse()
my_position = -1
wolf_position = animal_list.index("wolf")

if wolf_position == my_position + 1:
    print("Please go away and stop eating my sheep")

else:
    print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!")
