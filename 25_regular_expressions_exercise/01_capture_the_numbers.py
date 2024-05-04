import re

while True:
    lines = input()
    regex = r"\d+"
    matches = re.findall(regex, lines)
    if lines:
        if matches:
            print(" ".join(matches), end=" ")
    else:
        break
