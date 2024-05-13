import re

barcode_num = int(input())
product_dict = {}

valid_pattern = r"\@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+"

for x in range(barcode_num):
    barcode = input()
    valid_matches = re.findall(valid_pattern, barcode)
    if valid_matches:
        for match in valid_matches:
            digit_flag = False
            product_dict[match] = ""
            for symbol in match:
                if symbol.isdigit():
                    product_dict[match] += symbol
                    digit_flag = True
            if not digit_flag:
                product_dict[match] = "00"
            print(f"Product group: {product_dict[match]}")
    else:
        print("Invalid barcode")
