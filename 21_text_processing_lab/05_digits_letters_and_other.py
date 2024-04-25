def digits_letters_other(s):

    d = ""
    l = ""
    o = ""

    for symbol in s:

        if symbol.isdigit():
            d += symbol

        elif symbol.isalpha():
            l += symbol

        else:
            o += symbol
          
    return print(
                f"{d}\n"
                f"{l}\n"
                f"{o}\n"
    )


digits_letters_other(input())
