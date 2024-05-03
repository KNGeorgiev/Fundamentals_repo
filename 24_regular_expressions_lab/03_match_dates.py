import re

pattern = r"(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})"
text = input()
matches = re.findall(pattern, text)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
