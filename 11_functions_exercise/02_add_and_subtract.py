def add_and_subtract(a, b, c):

    def sum_numbers(a, b):
        sum_num = a + b
        return sum_num

    def subtract(c):
        sub_num = sum_numbers(a, b) - c
        return sub_num

    return print(subtract(c))


add_and_subtract(int(input()), int(input()), int(input()))
