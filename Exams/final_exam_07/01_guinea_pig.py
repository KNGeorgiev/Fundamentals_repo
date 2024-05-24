food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())
days = 0

while True:
    days += 1
    food -= 0.300

    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break

    if days % 2 == 0:
        daily_hay = food * 0.05
        hay -= daily_hay

    if days % 3 == 0:
        cover -= (weight / 3)

    if days == 30:
        print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
        break
        
