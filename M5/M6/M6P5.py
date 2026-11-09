# M6P5 - Employee Bonus
# Input: Employee last name, salary, job level
# Processing: Choose bonus rate based on job level;
#             bonus = salary * bonus_rate
# Output: Employee last name, bonus

last_name = input("Enter the employee last name: ")
salary = float(input("Enter the salary: "))
job_level = int(input("Enter the job level: "))

if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

print("Employee last name:", last_name)
print(f"{'Bonus:':<22}${bonus:>12.2f}")
