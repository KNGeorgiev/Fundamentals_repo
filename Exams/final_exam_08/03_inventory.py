inventory = input().split(", ")

while True:

    command = input().split(" - ")

    if command[0] == "Craft!":
        print(", ".join(inventory))
        break

    elif command[0] == "Collect" and command[1] not in inventory:
        inventory.append(command[1])

    elif command[0] == "Drop" and command[1] in inventory:
        inventory.remove(command[1])

    elif command[0] == "Combine Items":
        items = command[1].split(":")
        if items[0] in inventory:
            old_item_idx = inventory.index(items[0])
            inventory.insert(old_item_idx + 1, items[1])

    elif command[0] == "Renew" and command[1] in inventory:
        inventory.remove(command[1])
        inventory.append(command[1])
