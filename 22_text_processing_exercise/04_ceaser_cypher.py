def caesar_cipher(text):

    result = ""

    for symbol in text:
        result += chr(ord(symbol) + 3)

    return print(result)


input_line = input()
caesar_cipher(input_line)
