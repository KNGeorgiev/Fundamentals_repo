n = int(input())

for num in range(1, n + 1):
    total = 0
    digit = num

    while digit > 0:
        total += digit % 10
        digit = digit // 10

    if total == 5 or total == 7 or total == 11:
        print(f"{num} -> True")

    else:
        print(f"{num} -> False")
