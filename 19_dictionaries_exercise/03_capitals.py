countries = input().split(", ")
capitals = input().split(", ")

dictionary = dict(zip(countries, capitals))

for key, value in dictionary.items():
    print(f"{key} -> {value}")
