judge = {}

while True:

    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in judge.keys():
        judge[contest] = {username: points}

    else:
        if username not in judge[contest]:
            judge[contest].update({username: points})
        else:
            if points > judge[contest][username]:
                judge[contest][username] = points

sorted_score = {}
for competition, users in judge.items():
    print(f"{competition}: {len(users)} participants")
    counter = 0
    for name in users:
        sorted_score = {val[0]: val[1] for val in sorted(users.items(), key=lambda x: (-x[1], x[0]))}

    for key, value in sorted_score.items():
        counter += 1
        print(f"{counter}. {key} <::> {value}")

individual_standings = {}
for students in judge.values():
    for student, pts in students.items():
        if student not in individual_standings.keys():
            individual_standings[student] = [int(pts)]
        else:
            individual_standings[student].append(int(pts))

individual_standings = {k: sum(y) for k, y in individual_standings.items()}
sorted_standings = {val[0]: val[1] for val in sorted(individual_standings.items(), key=lambda x: (-x[1], x[0]))}
count = 0

print("Individual standings:")
for key, value in sorted_standings.items():
    count += 1
    print(f"{count}. {key} -> {value}")
