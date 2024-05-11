import re

input_line = input()
pattern = r"(\=|\/)([A-Z][a-zA-Z]{2,})\1"
match = re.finditer(pattern, input_line)
travel_points = 0
travel_list = []

for m in match:
    location = m[2]
    travel_points += len(location)
    travel_list.append(location)

travel_list = ", ".join(travel_list)

print(f"Destinations: {travel_list}")
print(f"Travel Points: {travel_points}")
