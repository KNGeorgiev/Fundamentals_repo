def pass_validator(p):
    flag = True
    digit_counter = 0

    if len(p) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        flag = False
    else:
        pass

    for i in p:
        if ord(i) not in range(65, 91) and ord(i) not in range(97, 123) and ord(i) not in range(48, 58):
            print("Password must consist only of letters and digits")
            flag = False
        else:
            pass

    for n in p:
        if ord(n) in range(48, 58):
            digit_counter += 1

    if digit_counter < 2:
        print("Password must have at least 2 digits")
        flag = False
    else:
        pass

    if flag:
        print("Password is valid")


password_string = input()
pass_validator(password_string)
