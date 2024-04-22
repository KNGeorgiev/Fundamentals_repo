n = int(input())
parking_lot = {}

for i in range(n):

    command = input().split()

    if command[0] == "register":
        username = command[1]
        license_plate_num = command[2]
        if username not in parking_lot:
            parking_lot[username] = license_plate_num
            print(f"{username} registered {license_plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")

    if command[0] == "unregister":
        username = command[1]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot[username]
            print(f"{username} unregistered successfully")
        pass

for user, lp in parking_lot.items():
    print(f"{user} => {lp}")
  
