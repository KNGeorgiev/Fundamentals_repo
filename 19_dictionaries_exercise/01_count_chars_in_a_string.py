text = input()
dictionary = {}

for symbol in text:

    key = symbol

    if key not in dictionary.keys() and symbol != " ":
        dictionary[key] = 1

    elif key in dictionary.keys() and symbol != " ":
        dictionary[key] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
