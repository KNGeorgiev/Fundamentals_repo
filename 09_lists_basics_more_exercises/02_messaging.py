sequence = input().split(" ")
text = input()
index_list = []
final_list = []
final = ""
for x in sequence:
    index_value = 0
    for y in x:
        index_value += int(y)
    index_list.append(index_value)

for z in index_list:
    real_index_value = 0
    real_index_value = z % len(text)
    final_list.append(text[real_index_value])
    text = text[:real_index_value] + text[real_index_value + 1:]

for letter in final_list:
    final += letter

print(final)
