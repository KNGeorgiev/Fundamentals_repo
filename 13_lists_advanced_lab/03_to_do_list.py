empty_note_list = [0] * 10

while True:

    text = input().split('-')

    if text[0] == 'End':
        break

    position = int(text[0]) - 1
    task = text[1]
    empty_note_list.pop(position)
    empty_note_list.insert(position, task)

final_list = [element for element in empty_note_list if element != 0]
print(final_list)
