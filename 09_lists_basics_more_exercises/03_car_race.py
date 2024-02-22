sequence = input().split(" ")
first_racer = []
second_racer = []
count_list = len(sequence)
half_list = count_list // 2
race1 = 0
race2 = 0
for first in range(0, half_list):
    first_racer.append(int(sequence[first]))

for second in range(half_list + 1, count_list):
    second_racer.append(int(sequence[second]))

for first_racer_lap in first_racer:
    race1 += first_racer_lap
    if first_racer_lap == 0:
        race1 = race1 * 0.8

second_racer.reverse()

for second_racer_lap in second_racer:
    race2 += second_racer_lap
    if second_racer_lap == 0:
        race2 = race2 * 0.8

if race1 < race2:
    print(f"The winner is left with total time: {race1:.1f}")
else:
    print(f"The winner is right with total time: {race2:.1f}")
