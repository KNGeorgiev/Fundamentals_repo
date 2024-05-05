import re

total_income = 0

while True:
    command = input()

    if command == "end of shift":
        break

    else:
        pattern = r"\%(?P<NAME>[A-Z][a-z]+)\%[^\.\%\$\|]*\<(?P<CONSUMABLE>\w+)\>[^\.\%\$\|]*\|(?P<QUANTITY>\d+)\|[^\.\%\$\|]*(?P<PRICE>[1-9][\.\d]*)\$"
        customer_data = re.search(pattern, command)

        if customer_data:
            name = customer_data.group(1)
            consumable = customer_data.group(2)
            quantity = customer_data.group(3)
            price = customer_data.group(4)
            total_price = float(price) * int(quantity)
            total_income += total_price
            print(f"{name}: {consumable} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")
