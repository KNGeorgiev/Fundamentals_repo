offerings = input().split(", ")
offerings_int = []
beggars_num = int(input())
total = []

for price in offerings:
    price_as_int = (int(price))
    offerings_int.append(price_as_int)

counter = 0

for x in range(1, beggars_num + 1):

    price_container = 0

    for y in range(counter, len(offerings_int), beggars_num):
        price_container += offerings_int[y]

    counter += 1
    total.append(price_container)

print(total)

