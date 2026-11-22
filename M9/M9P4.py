# M9P4 - Employee Gross Pay
def determine_pay_rate(job_code):
    if job_code == "L":
        return 25.0
    elif job_code == "A":
        return 30.0
    else:
        return 50.0


total_gross_pay = 0.0
response = input("Do you want to enter an employee? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Enter the employee's last name: ")
    job_code = input("Enter the job code (L/A/J): ").strip().upper()
    while job_code not in ("L", "A", "J"):
        job_code = input("Enter L, A, or J: ").strip().upper()
    hours = float(input("Enter the hours worked: "))
    rate = determine_pay_rate(job_code)
    if hours > 40:
        gross_pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross_pay = hours * rate
    total_gross_pay += gross_pay
    print(f"Last name: {last_name}")
    print(f"Gross pay: ${gross_pay:,.2f}")
    response = input("Do you want to enter another employee? (Yes/No): ").strip().lower()

print(f"Total gross pay: ${total_gross_pay:,.2f}")
