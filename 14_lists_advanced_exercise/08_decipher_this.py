message = input().split(' ')
first_letters_final = []
letters_list_final = []
final_message = ''
swapped_list = []

for word in message:
    word_as_list = [x for x in word]

    first_letters_raw = [y for y in word_as_list if y.isdigit() is True]
    first_letters_final.append(chr(int(''.join(first_letters_raw))))

    letters_list_raw = [z for z in word_as_list if z.isalpha() is True]
    letters_list_final.append(''.join(letters_list_raw))

for word in letters_list_final:
    first_letter = word[-1]
    last_letter = word[0]
    if len(word) == 1:
        new_word = word
        swapped_list.append(new_word)
    else:
        new_word = first_letter + word[1:-1] + last_letter
        swapped_list.append(new_word)

for first_letter in first_letters_final:
    first_letter += swapped_list[first_letters_final.index(first_letter)]
    final_message += first_letter + ' '

print(final_message)
