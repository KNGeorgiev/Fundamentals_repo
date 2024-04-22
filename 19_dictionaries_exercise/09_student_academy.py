student_grades = {}
n = int(input())

for i in range(n):
    name = input()
    grade = float(input())

    if name not in student_grades:
        student_grades[name] = [grade]
    else:
        student_grades[name].append(grade)

for student in student_grades:
    student_average = sum(student_grades[student]) / len(student_grades[student])
    if student_average >= 4.50:
        print(f"{student} -> {student_average:.2f}")
