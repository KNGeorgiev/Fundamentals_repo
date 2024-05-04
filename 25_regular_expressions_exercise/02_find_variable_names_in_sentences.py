import re

line = input()
pattern = r"(?<=\s_)[A-Za-z]*\b"
matches = re.findall(pattern, line)

print(",".join(matches))
