def repeat_strings(il):

    result = ""

    for word in il:
        for repeat in range(len(word)):
            result += word

    return print(result)


repeat_strings((input().split(" ")))
