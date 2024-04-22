company_users = {}

while True:
    command = input().split(" -> ")

    if command[0] == "End":
        break

    else:
        company_name = command[0]
        user_id = command[1]

        if company_name not in company_users:
            company_users[company_name] = [user_id]
        else:
            if user_id not in company_users[company_name]:
                company_users[company_name].append(user_id)

for company in company_users:
    print(company)
    for user in company_users[company]:
        print(f"-- {user}")
