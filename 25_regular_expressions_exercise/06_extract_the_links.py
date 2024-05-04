import re

input_line = input()
pattern = r"(www\.)([A-Za-z0-9\.\-]+)(\.[a-z]+[\.]*)"
valid_urls = []

while input_line:
    matches = re.search(pattern, input_line)
    if matches:
        valid_urls.append(matches[0])
    input_line = input()

for site in valid_urls:
    print("".join(site))
