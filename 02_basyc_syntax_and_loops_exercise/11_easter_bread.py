budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = (flour_price + flour_price * 0.25) / 4
bread = 0
colored_eggs = 0
total = 0

while budget >= total:

    total += (flour_price + egg_price + milk_price)
    bread += 1
    colored_eggs += 3

    if total > budget:
        total -= (flour_price + egg_price + milk_price)
        bread -= 1
        colored_eggs -= 3
        break

    if bread % 3 == 0:
        colored_eggs -= (bread - 2)

print(f"You made {bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget - total:.2f}BGN left.")
