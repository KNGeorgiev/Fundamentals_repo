import re

furniture = []
total_money = 0

while True:
    command = input()

    if command == "Purchase":
        break

    else:
        pattern = r">>(?P<ITEM>[A-Za-z]+)<<(?P<PRICE>\d+\.?\d*)\!(?P<QUANTITY>\d+)"
        matches = re.search(pattern, command)
        if matches:
            item = matches.group("ITEM")
            price = matches.group("PRICE")
            quantity = matches.group("QUANTITY")
            furniture.append(item)
            total_money += float(price) * int(quantity)

print(f"Bought furniture:")
for i in furniture:
    print(i)
print(f"Total money spend: {total_money:.2f}")
