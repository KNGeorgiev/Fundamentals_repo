text = input().split(' ')

while True:
    command = input().split(' ')

    if command[0] == '3:1':
        break

    elif command[0] == 'merge':
        start = int(command[1])
        finish = int(command[2])
        if start < 0:
            start = 0
        if finish > len(text) - 1:
            finish = len(text) - 1
        for index, string in enumerate(text):
            if index in range(start + 1, finish + 1):
                text[start] += text[index]
        for index in range(finish, start, - 1):
            text.pop(index)

    elif command[0] == 'divide':
        el_to_divide = text[int(command[1])]

        divisor = len(text[int(command[1])]) // int(command[2])

        divided = [el_to_divide[el:el + divisor] for el in
                   range(0, len(el_to_divide), divisor)]

        while len(divided) != int(command[2]):
            divided[-2] += divided[-1]
            divided.pop()

        text.pop(int(command[1]))

        for x in reversed(divided):
            text.insert(int(command[1]), x)


print(' '.join(text))
