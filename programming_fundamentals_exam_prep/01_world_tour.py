tour = input()

while True:
    command = input().split(":")

    if command[0] == "Travel":
        print(f"Ready for world tour! Planned stops: {tour}")
        break

    elif command[0] == "Add Stop":
        idx = int(command[1])
        spring = command[2]
        if idx < len(tour):
            tour = tour[:idx] + spring + tour[idx:]
        print(tour)

    elif command[0] == "Remove Stop":
        start = int(command[1])
        finish = int(command[2])
        if 0 <= (start and finish) < len(tour):
            tour = tour[:start] + tour[finish + 1:]
        print(tour)

    elif command[0] == "Switch":
        old = command[1]
        new = command[2]
        if old in tour:
            tour = tour.replace(old, new)
        print(tour)
