# M9P5 - Student Tuition
def compute_tuition(credit_hours, district_code):
    if district_code == "I":
        cost_per_credit = 250.0
    else:
        cost_per_credit = 550.0
    return credit_hours * cost_per_credit


total_tuition = 0.0
response = input("Do you want to enter a student? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Enter the student's last name: ")
    credit_hours = int(input("Enter the credit hours: "))
    district_code = input("Enter the district code (I/O): ").strip().upper()
    while district_code not in ("I", "O"):
        district_code = input("Enter I or O: ").strip().upper()
    tuition = compute_tuition(credit_hours, district_code)
    total_tuition += tuition
    print(f"Last name: {last_name}")
    print(f"Tuition owed: ${tuition:,.2f}")
    response = input("Do you want to enter another student? (Yes/No): ").strip().lower()

print(f"Total tuition owed: ${total_tuition:,.2f}")
