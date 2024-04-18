number = int(input())
dictionary = {}

for x in range(number):

    word = input()
    synonym = input()

    if word not in dictionary.keys():
        dictionary[word] = [synonym]

    else:
        dictionary[word].append(synonym)

for key, value in dictionary.items():
    print(f"{key} - {', '.join(value)}")
