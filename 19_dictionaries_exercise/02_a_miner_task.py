dictionary = {}

while True:

    resource_type = input()

    if resource_type == "stop":
        break

    resource_value = int(input())

    if resource_type not in dictionary.keys():
        dictionary[resource_type] = resource_value

    else:
        dictionary[resource_type] += resource_value

for key, value in dictionary.items():
    print(f"{key} -> {value}")
