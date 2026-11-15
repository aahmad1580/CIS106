# M8P5 - Student Tuition
from pathlib import Path

data_file = Path(__file__).with_name("M8P5_Students.txt")
total_tuition = 0.0
student_count = 0

print(f"{'Last Name':<16}{'Credits':>10}{'Tuition Owed':>17}")

with data_file.open(encoding="utf-8") as students:
    for line in students:
        last_name = line.strip()
        district_code = students.readline().strip().upper()
        credits = int(students.readline())

        if district_code == "I":
            cost_per_credit = 250.00
        else:
            cost_per_credit = 500.00

        tuition = credits * cost_per_credit
        total_tuition += tuition
        student_count += 1

        tuition_display = f"${tuition:,.2f}"
        print(f"{last_name:<16}{credits:>10}{tuition_display:>17}")

print(f"\nTotal tuition owed: ${total_tuition:,.2f}")
print(f"Number of students: {student_count}")
