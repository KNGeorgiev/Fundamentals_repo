number_of_rows = int(input())
field = []
destroyed = 0

for i in range(number_of_rows):
    field.append(list(map(int, input().split(' '))))

attacks = input().split(' ')

for atk in attacks:
    atk = atk.split('-')
    atk_x = int(atk[0])
    atk_y = int(atk[1])

    if field[atk_x][atk_y] != 0:
        field[atk_x][atk_y] -= 1
        if field[atk_x][atk_y] == 0:
            destroyed += 1

print(destroyed)
