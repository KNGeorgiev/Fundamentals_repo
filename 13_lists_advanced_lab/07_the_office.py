employees_list = input().split(" ")
happiness_factor = int(input())

employees_list = list(map(lambda x: int(x) * happiness_factor, employees_list))
filtered_list = list(filter(lambda x: x >= (sum(employees_list) / len(employees_list)), employees_list))

if len(filtered_list) >= len(employees_list) / 2:
    print(f"Score: {len(filtered_list)}/{len(employees_list)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_list)}/{len(employees_list)}. Employees are not happy!")
