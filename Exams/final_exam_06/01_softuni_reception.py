employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
student_num = int(input())
hours = 0

while student_num > 0:

    hours += 1
    if hours % 4 == 0:
        pass
    else:
        total_students_per_hour = employee_1 + employee_2 + employee_3
        student_num -= total_students_per_hour

print(f"Time needed: {hours}h.")
