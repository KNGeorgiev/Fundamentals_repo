def replace_repeating_chars(text):

    result = ""
    last_symbol = ""

    for symbol in text:
        if symbol != last_symbol:
            result += symbol
            last_symbol = symbol

    return print(result)


input_line = input()
replace_repeating_chars(input_line)
