word1 = input()
word2 = input()

result = word1

for i in range(len(word1)):

    if word1[i] == word2[i]:
        continue

    result = word2[:i + 1] + word1[i + 1:]
    print(result)
