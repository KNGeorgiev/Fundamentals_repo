import sys

factor = int(input())
count = int(input())
multiples_list = []

for x in range(count):
    if factor == 1:
        for y in range(factor, count + 1):
            multiples_list.append(y)
        break

    else:
        for y in range(1, sys.maxsize):

            if y % factor == 0 and factor != 1:
                multiples_list.append(y)

            if len(multiples_list) == count:
                break

print(multiples_list)
