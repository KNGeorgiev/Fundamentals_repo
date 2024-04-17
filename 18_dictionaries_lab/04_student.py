students = {}

while True:

    student_data = input().split(":")

    if len(student_data) == 1:
        student_data[0] = student_data[0].replace("_", " ")
        personal_data = students[student_data[0]]
        for data in personal_data:
            for key, value in data.items():
                print(f"{key} - {value}")
        break

    else:
        name = student_data[0]
        student_id = student_data[1]
        course_type = student_data[2]
        if course_type not in students:
            students[course_type] = [{name: student_id}]
        else:
            students[course_type].append({name: student_id})
