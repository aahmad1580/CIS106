# M3P2 - Exam Points
# IPO Chart
# Input: Last name, midterm score, final score
# Processing: total_points = midterm * 0.40 + final * 0.60
# Output: Last name, total exam points

last_name = input("Enter the student's last name: ")
midterm = float(input("Enter the midterm score (0-100): "))
final = float(input("Enter the final exam score (0-100): "))

total_points = midterm * 0.40 + final * 0.60

print("Last name:", last_name)
print(f"Total exam points: {total_points:.2f}")
