text_list = input().split(' ')

final_list = [x for x in text_list if len(x) % 2 == 0]

print(*final_list, sep='\n')
