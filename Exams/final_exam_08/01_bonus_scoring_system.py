student_number = int(input())
total_lectures = int(input())
bonus = int(input())
student_class = {}

if total_lectures == 0:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")

else:
    for student in range(student_number):
        attendance_num = int(input())
        total_bonus = attendance_num / total_lectures * (5 + bonus)
        student_class[total_bonus] = attendance_num

    print(f"Max Bonus: {round(max(student_class.keys()))}.")
    print(f"The student has attended {max(student_class.values())} lectures.")
