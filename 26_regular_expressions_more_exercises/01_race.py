import operator
import re

participants = input().split(", ")
filtered = {}

while True:
    command = input()

    if command == "end of race":
        break

    else:
        name_pattern = r"[A-Za-z]"
        distance_pattern = r"[\d+]"
        name = re.findall(name_pattern, command)

        distance = re.findall(distance_pattern, command)
        distance = [int(x) for x in distance]
        distance = sum(distance)

        if name:
            racer = "".join(name)
            if racer in participants:
                if racer in filtered:
                    filtered[racer] += distance
                else:
                    filtered[racer] = distance

filtered = sorted(filtered.items(), key=operator.itemgetter(1), reverse=True)

print(f"1st place: {filtered[0][0]}")
print(f"2nd place: {filtered[1][0]}")
print(f"3rd place: {filtered[2][0]}")
