orders_number = int(input())
total = 0

for x in range(1, orders_number + 1):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= capsule_price <= 100 and days in range(1, 32) and capsules_per_day in range(1, 2001):
        total_capsule_price = capsule_price * days * capsules_per_day
        total += total_capsule_price
        print(f"The price for the coffee is: ${total_capsule_price:.2f}")

    else:
        continue

print(f"Total: ${total:.2f}")
