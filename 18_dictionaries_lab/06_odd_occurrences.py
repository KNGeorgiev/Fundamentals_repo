elements = {}
sequence = input().split(" ")

for x in sequence:
    x_low = x.lower()
    if x_low not in elements:
        elements[x_low] = 0
    elements[x_low] += 1

for key, value in elements.items():
    if value % 2 != 0:
        print(key, end=" ")
