# M7P4 - Employee Pay
total_gross_pay = 0.0
employee_count = 0
answer = input("Do you want to enter an employee's pay data? (Yes/No): ")

while answer.strip().lower() == "yes":
    last_name = input("Enter the employee's last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly pay rate: "))

    if hours > 40:
        gross_pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross_pay = hours * rate

    total_gross_pay += gross_pay
    employee_count += 1

    print(f"Last name: {last_name}")
    print(f"Gross pay: ${gross_pay:.2f}")
    answer = input("Do you want to enter another employee? (Yes/No): ")

average_pay = 0.0
if employee_count > 0:
    average_pay = total_gross_pay / employee_count

print(f"Total gross pay: ${total_gross_pay:.2f}")
print(f"Number of employees: {employee_count}")
print(f"Average pay: ${average_pay:.2f}")
