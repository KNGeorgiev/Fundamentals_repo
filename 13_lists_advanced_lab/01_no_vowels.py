word = input()
word_as_list = [x for x in word]
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
no_vowels = [x for x in word_as_list if x not in vowels]
print(*no_vowels, sep='')
