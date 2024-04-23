contests = {}
submissions = {}

while True:
    first_command = input()
    if first_command == "end of contests":
        break
    else:
        contest, contest_password = first_command.split(":")
        contests[contest] = contest_password

while True:
    second_command = input()
    if second_command == "end of submissions":
        break
    else:
        contest, contest_password, username, points = second_command.split("=>")
        points = int(points)
        if contest in contests:
            if contests[contest] == contest_password:
                if username not in submissions:
                    submissions[username] = [[contest], [points]]
                else:
                    if contest in submissions[username][0]:
                        ctst_idx = submissions[username][0].index(contest)
                        if points > submissions[username][1][ctst_idx]:
                            submissions[username][1][ctst_idx] = points
                    else:
                        submissions[username][0].append(contest)
                        submissions[username][1].append(points)

total_points = {}
best_candidate = ""
max_points = 0

for key, value in submissions.items():
    total_points[key] = (sum(value[1]))

for key, value in total_points.items():
    if value > max_points:
        max_points = value
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")

for key, value in sorted(submissions.items()):
    print(f"{key}")
    for v in range(len(value[0])):
        current_max = max(value[1])
        index_current_max = value[1].index(current_max)
        print(f"#  {value[0][index_current_max]} -> {current_max}")
        value[1][index_current_max] = -1
