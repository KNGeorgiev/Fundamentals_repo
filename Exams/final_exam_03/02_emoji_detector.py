import re

text = input()

cool_threshold = 1
cool_pattern = r"\d"
cool_list = re.findall(cool_pattern, text)
for match in cool_list:
    cool_threshold *= int(match)

emoji_pattern = r"(\*{2}|\:{2})([A-Z][a-z]{2,})\1"
emoji_list = re.finditer(emoji_pattern, text)
emoji_list = [match.group() for match in emoji_list]

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
result_pattern = r'[A-z]'

for emoji in emoji_list:
    coolness = 0
    result_match = re.findall(result_pattern, emoji)
    for match in result_match:
        coolness += ord(match)
    if coolness >= cool_threshold:
        print(emoji)
