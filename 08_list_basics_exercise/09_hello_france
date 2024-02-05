collection_of_items = input().split("|")
budget = float(input())
sell = []
profit = []

for x in range(len(collection_of_items)):

    x_list = collection_of_items[x].split("->")
    type_list_x = x_list[0]
    price_list_x = float(x_list[1])

    if type_list_x == "Clothes" and price_list_x <= 50.00:
        if budget >= price_list_x:
            budget -= price_list_x
            sell.append(price_list_x + price_list_x * 0.40)
            profit.append(price_list_x * 0.40)

    if type_list_x == "Shoes" and price_list_x <= 35.00:
        if budget >= price_list_x:
            budget -= price_list_x
            sell.append(price_list_x + price_list_x * 0.40)
            profit.append(price_list_x * 0.40)

    if type_list_x == "Accessories" and price_list_x <= 20.50:
        if budget >= price_list_x:
            budget -= price_list_x
            sell.append(price_list_x + price_list_x * 0.40)
            profit.append(price_list_x * 0.40)

for y in sell:
    print(f"{y:.2f}", end=(" "))

print("")
print(f"Profit: {sum(profit):.2f}")

if sum(sell) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
