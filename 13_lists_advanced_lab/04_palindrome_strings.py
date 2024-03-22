sequence = input().split(' ')
palindrome_word = input()
palindrome_list = []

for word in sequence:

    if word == word[::-1]:
        palindrome_list.append(word)

print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome_word)} times')
