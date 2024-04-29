input_line = input().upper()
symbol_num = ""
rage_line = ""
combo = ""
num = ""

for index, symbol in enumerate(input_line):09_

    if not symbol.isdigit():
        if symbol not in symbol_num:
            symbol_num += symbol

        combo += symbol

    else:
        num += symbol
        if index == len(input_line) - 1:
            rage_line += int(num) * combo

        elif index < len(input_line) - 1:
            if not input_line[index + 1].isdigit():
                rage_line += int(num) * combo
                combo = ""
                num = ""


print(f"Unique symbols used: {len(symbol_num)}")
print(rage_line)
