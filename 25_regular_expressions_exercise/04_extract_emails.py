import re

line = input()
pattern = r"(?<=\s)(?P<USER>[a-z0-9]+[\.\-\_a-z0-9]*)(?P<HOST>@[a-z0-9-]+\.[a-z.]+)\b"
matches = re.findall(pattern, line)

for mail in matches:
    print("".join(mail))
