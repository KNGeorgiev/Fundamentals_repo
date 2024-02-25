fire_data_input = input().split("#")
water_amount = int(input())
effort = 0
fire_value_list = []

for x in range(len(fire_data_input)):

    x_list = fire_data_input[x].split()
    x_fire_type = x_list[0]
    x_fire_value = int(x_list[2])

    if x_fire_type == "High" and x_fire_value in range(81, 126):
        if water_amount >= x_fire_value:
            fire_value_list.append(x_fire_value)
            effort += x_fire_value * 0.25
            water_amount -= x_fire_value

    elif x_fire_type == "Medium" and x_fire_value in range(51, 81):
        if water_amount >= x_fire_value:
            fire_value_list.append(x_fire_value)
            effort += x_fire_value * 0.25
            water_amount -= x_fire_value

    elif x_fire_type == "Low" and x_fire_value in range(1, 51):
        if water_amount >= x_fire_value:
            fire_value_list.append(x_fire_value)
            effort += x_fire_value * 0.25
            water_amount -= x_fire_value

print("Cells:")
for p in fire_value_list:
    print(f" - {p}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(fire_value_list)}")
