sequence = input().split(', ')


def palindrome_integers(l):

    for element in l:
        if element == ''.join(reversed(element)):
            print(True)
        else:
            print(False)


palindrome_integers(sequence)
