string = input()
list_string = string.split(" ")
list_num = []

for i in list_string:
    i = int(i)
    i = i * -1
    list_num.append(i)

print(list_num)
