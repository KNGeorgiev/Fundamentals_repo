results = {}
submissions = {}

while True:
    user_data = input().split("-")

    if user_data[0] == "exam finished":
        break

    username = user_data[0]
    language = user_data[1]

    if username in results and user_data[1] == "banned":
        del results[username]

    else:
        points = int(user_data[2])
        if username not in results and language not in submissions:
            results[username] = [points]
            submissions[language] = 1

        elif username in results and language in submissions:
            results[username].append(points)
            top_result = max(results[username])
            results[username] = [top_result]
            submissions[language] += 1

        elif username not in results and language in submissions:
            results[username] = [points]
            submissions[language] += 1

print("Results:")
for key, value in results.items():
    value_as_str = max(value)
    value_as_str = str(value_as_str)
    print(f"{key} | {''.join(value_as_str)}")

print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
