# M8P3 - Employee Bonuses
from pathlib import Path

data_file = Path(__file__).with_name("M8P3_Employees.txt")
total_bonuses = 0.0

print(f"{'Last Name':<16}{'Salary':>15}{'Bonus':>15}")

with data_file.open(encoding="utf-8") as employees:
    for line in employees:
        last_name = line.strip()
        salary = float(employees.readline())

        if salary >= 100000.00:
            bonus_rate = 0.20
        elif salary == 50000.00:
            bonus_rate = 0.15
        else:
            bonus_rate = 0.10

        bonus = salary * bonus_rate
        total_bonuses += bonus
        salary_display = f"${salary:,.2f}"
        bonus_display = f"${bonus:,.2f}"
        print(f"{last_name:<16}{salary_display:>15}{bonus_display:>15}")

print(f"\nTotal bonuses paid: ${total_bonuses:,.2f}")
