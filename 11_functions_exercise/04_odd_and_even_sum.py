def sum_of_digits(n):
    even_list = []
    odd_list = []

    for i in n:
        if int(i) % 2 == 0:
            even_list.append(int(i))
        else:
            odd_list.append(int(i))

    print(f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}")


sum_of_digits(input())
