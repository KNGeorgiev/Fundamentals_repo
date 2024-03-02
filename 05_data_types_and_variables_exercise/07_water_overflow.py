lines = int(input())
tank_capacity = 255
storage = 0

for x in range(lines):
    litres = int(input())
    storage += litres
    if tank_capacity < storage:
        print("Insufficient capacity!")
        storage -= litres

print(storage)
