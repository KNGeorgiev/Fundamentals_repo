def text_filter(forbidden, txt):

    forbidden = forbidden.split(", ")

    for word in forbidden:
        while word in txt:
            txt = txt.replace(word, "*" * len(word))

    return print(txt)


f = input()
t = input()
text_filter(f, t)
