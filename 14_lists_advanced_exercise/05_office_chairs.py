n = int(input())
free_counter = 0
chair_deficit = 0

room_chair_list = [input().split(' ') for x in range(n)]

for x in room_chair_list:
    if len(x[0]) < int(x[1]):
        print(f"{int(x[1]) - len(x[0])} more chairs needed in room {room_chair_list.index(x) + 1}")
        chair_deficit += 1
    else:
        free_counter += (len(x[0]) - int(x[1]))

if free_counter >= 0 and chair_deficit == 0:
    print(f"Game On, {free_counter} free chairs left")

print(room_chair_list)
