lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

helmet_expenses = 0
sword_expenses = 0
shield_expenses = 0
shield_count = 0
armor_expenses = 0

for fight in range(1, lost_fights + 1):

    if fight % 2 == 0:
        helmet_expenses += helmet

    if fight % 3 == 0:
        sword_expenses += sword

    if fight % 3 == 0 and fight % 2 == 0:
        shield_expenses += shield
        shield_count += 1
        if shield_count % 2 == 0:
            armor_expenses += armor

total = helmet_expenses + sword_expenses + shield_expenses + armor_expenses
print(f"Gladiator expenses: {total:.2f} aureus")
