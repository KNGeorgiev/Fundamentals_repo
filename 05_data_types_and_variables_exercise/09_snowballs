snowball_number = int(input())
highest_value = 0
weight_value = 0
time_value = 0
quality_value = 0

for snowball in range(1, snowball_number + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    formula = (weight / time) ** quality

    if formula > highest_value:
        highest_value = formula
        weight_value = weight
        time_value = time
        quality_value = quality

print(f"{weight_value} : {time_value} = {round(highest_value)} ({quality_value})")
