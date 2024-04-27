def character_multiplier(input_line):

    word1, word2 = input_line.split(" ")
    result = 0

    if len(word1) < len(word2):
        idx = 0
        for x in range(len(word1)):
            result += ord(word1[idx]) * ord(word2[idx])
            idx += 1

        for y in range(idx, len(word2)):
            result += ord(word2[idx])
            idx += 1

    elif len(word2) < len(word1):
        idx = 0
        for x in range(len(word2)):
            result += ord(word2[idx]) * ord(word1[idx])
            idx += 1

        for y in range(idx, len(word1)):
            result += ord(word1[idx])
            idx += 1

    else:
        for x in range(len(word1)):
            result += ord(word1[x - 1]) * ord(word2[x - 1])

    return print(result)


command = input()
character_multiplier(command)
