l1 = input().split(", ")

for i in range(len(l1)):
    l1.append(l1.pop(l1.index("0")))

print([eval(x) for x in l1])
