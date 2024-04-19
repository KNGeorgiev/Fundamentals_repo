receipt = {}

command = input().split(" ")

while command[0] != "buy":

    name = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if name not in receipt:
        receipt[name] = [price, quantity]
    else:
        receipt[name][0] = price
        receipt[name][1] += quantity

    command = input().split(" ")

for key, value in receipt.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
