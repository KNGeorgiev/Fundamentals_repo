product = input()
qty = float(input())


def price_calculator(product, qty):

    if product == "coffee":
        cost = qty * 1.50

    elif product == "coke":
        cost = qty * 1.40

    elif product == "water":
        cost = qty * 1.00

    elif product == "snacks":
        cost = qty * 2.00

    return cost


print(f"{price_calculator(product, qty):.2f}")
