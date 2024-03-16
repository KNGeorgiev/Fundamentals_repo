first_row = input().split(" ")
second_row = input().split(" ")
third_row = input().split(" ")

tic_tac_toe = [first_row, second_row, third_row]
victory = False

for row in tic_tac_toe:
    if row[0] == row[1] == row[2] == "1":
        print("First player won")
        victory = True
        break
    elif row[0] == row[1] == row[2] == "2":
        print("Second player won")
        victory = True
        break

for x in first_row:
    for y in second_row:
        for z in third_row:
            if first_row.index(x) == second_row.index(y) == third_row.index(z):
                if x == y == z == "1":
                    print("First player won")
                    victory = True
                    break
                elif x == y == z == "2":
                    print("Second player won")
                    victory = True
                    break

for a in first_row:
    for b in second_row:
        for c in third_row:
            if first_row.index(a) == 0 and second_row.index(b) == 1 and third_row.index(c) == 2:
                if a == b == c == "1":
                    print("First player won")
                    victory = True
                    break
                elif a == b == c == "2":
                    print("Second player won")
                    victory = True
                    break

            elif first_row.index(a) == 2 and second_row.index(b) == 1 and third_row.index(c) == 0:
                if a == b == c == "1":
                    print("First player won")
                    victory = True
                    break
                elif a == b == c == "2":
                    print("Second player won")
                    victory = True
                    break

if not victory:
    print("Draw!")
