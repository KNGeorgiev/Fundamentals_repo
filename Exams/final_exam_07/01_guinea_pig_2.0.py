qty_food = float(input())
qty_hay = float(input())
qty_cover = float(input())
weight = float(input())

for i in range(1, 31):
    qty_food -= 0.300

    if qty_food <= 0 or qty_hay <= 0 or qty_cover <= 0:
        print("Merry must go to the pet store!")
        break

    if i % 2 == 0:
        qty_hay -= (qty_food * 0.05)

    if i % 3 == 0:
        qty_cover -= weight / 3

    if i == 30:
        if qty_food > 0 and qty_hay > 0 and qty_cover > 0:
            print(f"Everything is fine! Puppy is happy! Food: {qty_food:.2f}, Hay: {qty_hay:.2f}, Cover: {qty_cover:.2f}.")
            break
        else:
            print("Merry must go to the pet store!")
            break
