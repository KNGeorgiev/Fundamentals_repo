import re

demon_input = re.split(", *", input())
demon_input = [demon.strip() for demon in demon_input]
demon_dict = {}

health_pattern = r"[^0-9\+\-\*\/\.]"
damage_pattern = r"((\+|\-)?(\d+)(\.\d+)?)"
operator_pattern = r"[\*\/]"

for demon in demon_input:

    health = 0
    damage = 0

    health_match = re.findall(health_pattern, demon)
    damage_match = re.finditer(damage_pattern, demon)
    operator_match = re.findall(operator_pattern, demon)

    for hp in health_match:
        health += ord(hp)

    for dmg in damage_match:
        damage += float(dmg.group())

    for operator in operator_match:
        if operator == "*":
            damage *= 2
        elif operator == "/":
            damage /= 2

    demon_dict[demon] = {"health": health, "damage": damage}

for demon in sorted(demon_dict):
    print(f"{demon} - {demon_dict[demon]['health']} health, {demon_dict[demon]['damage']:.2f} damage")
