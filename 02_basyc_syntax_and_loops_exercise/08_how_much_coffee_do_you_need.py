command = input()
coffee_count = 0

while command != "END":

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_count += 1

    if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_count += 2

    command = input()

if coffee_count <= 5:
    print(coffee_count)

if coffee_count > 5:
    print("You need extra sleep")
