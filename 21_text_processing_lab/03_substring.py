def substring(first, second):

    while True:

        if first in second:
            second = second.replace(first, "")

        else:
            break

    return print(second)


first_string = input()
second_string = input()
substring(first_string, second_string)
