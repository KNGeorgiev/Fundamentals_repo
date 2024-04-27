def emoticon_finder(text):

    result = []

    for index, symbol in enumerate(text):
        if symbol == ":":
            result.append(":" + text[index + 1])

    for emoji in result:
        print(emoji)


input_line = input()
emoticon_finder(input_line)
