def len_checker(word):
    if 3 <= len(word) <= 16:
        return True
    return False


def symbol_checker(word):
    for symbol in word:
        if not (symbol.isalnum() or symbol == "-" or symbol == '_'):
            return False
    return True


def redundant_checker(word):
    if " " in word:
        return False
    return True


def username_validator(word):
    if len_checker(word) and symbol_checker(word) and redundant_checker(word):
        return True
    return False


usernames = input().split(', ')
for word in usernames:
    if username_validator(word):
        print(word)
