list_of_numbers = input().split(" ")
list_with_int = [eval(i) for i in list_of_numbers]
n = int(input())

for x in range(1, n + 1):
    list_with_int.remove(min(list_with_int))

print(", ".join([str(y) for y in list_with_int]))
