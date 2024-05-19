import re

text_string = input()
mirrors_dict = {}
mirrors_list = []

pattern = r"(\@+|\#+)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.findall(pattern, text_string)

matches = [(match[1], match[2]) for match in matches]

for m in matches:
   if m[0][::-1] == m[1]:
       mirrors_dict[m[0]] = m[1]

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if mirrors_dict:
    for k,v in mirrors_dict.items():
        mirrors_list.append(f"{k} <=> {v}")
    print("The mirror words are:")
    print(", ".join(mirrors_list))
else:
    print("No mirror words!")
