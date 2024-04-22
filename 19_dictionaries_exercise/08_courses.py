courses = {}
command = input().split(" : ")

while command[0] != "end":

    if len(command) > 1:
        course_name = command[0]
        student_name = command[1]

        if course_name not in courses:
            courses[course_name] = [student_name]
        else:
            courses[course_name].append(student_name)

    command = input().split(" : ")

for key, value in courses.items():
    student_count = len(value)
    print(f"{key}: {student_count}")
    for student in value:
        print(f"-- {''.join(student)}")
