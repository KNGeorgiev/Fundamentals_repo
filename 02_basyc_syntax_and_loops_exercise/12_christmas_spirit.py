ornament_set_price = 2
ornament_set_points = 5

tree_skirt_price = 5
tree_skirt_points = 3

tree_garland_price = 3
tree_garland_points = 10

tree_lights_price = 15
tree_lights_points = 17

quantity = int(input())
days = int(input())
days_counter = 0
budget = 0
spirit = 0

for i in range(1, days + 1):

    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        budget += ornament_set_price * quantity
        spirit += ornament_set_points

    if i % 3 == 0:
        budget += quantity * tree_skirt_price + quantity * tree_garland_price
        spirit += tree_skirt_points + tree_garland_points

    if i % 5 == 0:
        budget += quantity * tree_lights_price
        spirit += tree_lights_points

    if i % 5 == 0 and i % 3 == 0:
        spirit += 30

    if i % 10 == 0:
        budget += tree_garland_price + tree_skirt_price + tree_lights_price
        spirit -= 20

    if i == days and i % 10 == 0:
        spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
