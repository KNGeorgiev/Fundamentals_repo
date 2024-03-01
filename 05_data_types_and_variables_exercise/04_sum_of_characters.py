rows = int(input())
storage = 0

for i in range(rows):
    letter = input()
    letter_value = ord(letter)
    storage += letter_value

print(f"The sum equals: {storage}")
