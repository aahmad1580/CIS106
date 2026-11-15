# M7P3 - Exam Averages
student_count = 0
answer = input("Do you want to enter a student's scores? (Yes/No): ")

while answer.strip().lower() == "yes":
    last_name = input("Enter the student's last name: ")
    exam1 = float(input("Enter the first exam score: "))
    exam2 = float(input("Enter the second exam score: "))

    average = (exam1 + exam2) / 2
    student_count += 1

    print(f"Last name: {last_name}")
    print(f"Average exam score: {average:.2f}")
    answer = input("Do you want to enter another student? (Yes/No): ")

print(f"Number of students: {student_count}")
