products_in_stock = {}

while True:

    command = input().split(": ")

    if command[0] == "statistics":
        print("Products in stock:")

        for product_name, quantity in products_in_stock.items():
            print(f"- {product_name}: {quantity}")

        print(f"Total Products: {len(products_in_stock.keys())}")
        print(f"Total Quantity: {sum(products_in_stock.values())}")
        break

    else:
        product = command[0]
        qty = int(command[1])
        if product in products_in_stock:
            products_in_stock[product] += qty
        else:
            products_in_stock[product] = qty
            
