import re

message_num = int(input())
attack_list = []
destroy_list = []

for x in range(message_num):

    message_line = input()
    pattern = r"[s,t,a,r,S,T,A,R]"
    star_count = len(re.findall(pattern, message_line))
    message = ""

    for letter in message_line:
        message += chr(ord(letter) - star_count)

    split_pattern = (r"\@(?P<PLANET>[A-Za-z]+)[^\@\!\-\:]*"
                     r"\:(?P<POPULATION>[1-9][0-9]+)[^\@\!\-\:]*"
                     r"\!(?P<ATTACKTYPE>A|D)\![^\@\!\-\:]*"
                     r"\->(?P<SOLDIERS>[1-9][0-9]+)")

    star_data = re.search(split_pattern, message)

    if star_data:
        planet = star_data.group(1)
        population = star_data.group(2)
        attack_type = star_data.group(3)
        soldiers = star_data.group(4)

        if attack_type == "A":
            attack_list.append(planet)

        if attack_type == "D":
            destroy_list.append(planet)

attack_list = sorted(attack_list)
destroy_list = sorted(destroy_list)

print(f"Attacked planets: {len(attack_list)}")
for p in attack_list:
    print(f"-> {p}")

print(f"Destroyed planets: {len(destroy_list)}")
for p in destroy_list:
    print(f"-> {p}")
