a_counter = 0
b_counter = 0

red_card = input()
red_card_list = red_card.split(" ")
red_card_list = set(red_card_list)

for i in red_card_list:

    if "A" in i:
        a_counter += 1

    if "B" in i:
        b_counter += 1

    if a_counter > 4 or b_counter > 4:
        break

print(f"Team A - {11 - a_counter}; Team B - {11 - b_counter}")

if a_counter > 4 or b_counter > 4:
    print("Game was terminated")
