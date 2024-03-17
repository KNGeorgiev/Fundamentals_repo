def loading_bar(n):
    symbol_multiplier = n // 10
    empty_part = 10 - symbol_multiplier
    bar = (symbol_multiplier * '%') + (empty_part * '.')

    if empty_part == 0:
        print('100% Complete!')
        print(f'[{bar}]')
    else:
        print(f'{n}% [{bar}]')
        print('Still loading...')


loaded_percentage = int(input())
loading_bar(loaded_percentage)
