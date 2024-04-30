import re

key_combo = input().split()

while True:
    sequence = input()
    result = ""
    treasure = ""
    coordinates = ""

    if sequence == "find":
        break

    else:
        counter = 0
        for symbol in sequence:

            if counter == len(key_combo):
                counter = 0
            result += chr(ord(symbol) - int(key_combo[counter]))
            counter += 1

    treasure_pattern = "&.+&"
    coordinates_pattern = "<.+>"

    treasure_match = re.findall(treasure_pattern, result)
    coordinates_match = re.findall(coordinates_pattern, result)

    treasure = re.findall("\w", treasure_match[0])
    treasure = "".join(treasure)

    coordinates = re.findall("\w", coordinates_match[0])
    coordinates = "".join(coordinates)

    print(f"Found {treasure} at {coordinates}")
