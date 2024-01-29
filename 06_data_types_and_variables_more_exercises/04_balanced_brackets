lines = int(input())
balance = 0

for i in range(lines):
    symbol = input()

    if symbol == "(":
        balance += 1
        if balance > 1:
            break

    elif symbol == ")":
        balance -= 1
        if balance < 0:
            break

if balance == 0:
    print("BALANCED")

else:
    print("UNBALANCED")
