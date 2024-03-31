text_input = input()
result = ''

number_list = [int(num) for num in text_input if num.isdigit()]
take_list = number_list[::2]
skip_list = number_list[1::2]

non_number_list = [symbol for symbol in text_input if not symbol.isdigit()]

while len(take_list) > 0 or len(skip_list) > 0:
    take_count = take_list[0]
    skip_count = skip_list[0]

    if len(take_list) == 0:
        continue

    else:
        for i in range(take_count):
            result += non_number_list[0]
            non_number_list.pop(0)
        take_list.remove(take_count)

    for i in range(skip_count):
        non_number_list.pop(0)
    skip_list.remove(skip_count)

print(result)
