import re

numbers = input()

pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
numbers_match = re.findall(pattern, numbers)

print(", ".join(numbers_match))
