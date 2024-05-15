import re

input_line = input()
total_calories = 0
refrigerator = []

food_pattern = (r"(#|\|)(?P<FOOD>[A-Za-z\s]+)\1"
                r"(?P<EXPDATE>[0-9]{2}/[0-9]{2}/[0-9]{2})\1"
                r"(?P<CALORIES>[0-9]{1,5})\1")

extracted_data = re.finditer(food_pattern, input_line)

for match in extracted_data:
    food = match['FOOD']
    exp_date = match['EXPDATE']
    calories = match['CALORIES']
    total_calories += int(calories)
    refrigerator.append({'food': food,
                         'exp_date': exp_date,
                         'calories': calories})

print(f"You have food to last you for: {total_calories // 2000} days!")

for food in refrigerator:
    print(f"Item: {food['food']}, Best before: {food['exp_date']}, Nutrition: {food['calories']}")
