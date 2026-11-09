# M6P3 - CD Interest
# Input: Principal amount, years to maturity
# Processing: Choose interest rate using principal and years;
#             first_year_interest = principal * interest_rate
# Output: Principal, interest rate, first year interest

principal = float(input("Enter the principal amount: "))
years = int(input("Enter the years to maturity: "))

if principal > 100000 and years == 5:
    interest_rate = 0.06
elif principal >= 50000 and principal <= 100000:
    if years == 10:
        interest_rate = 0.05
    elif years == 5:
        interest_rate = 0.04
    else:
        interest_rate = 0.02
else:
    interest_rate = 0.02

first_year_interest = principal * interest_rate

print(f"{'Principal:':<22}${principal:>12.2f}")
print(f"{'Interest rate:':<22} {interest_rate * 100:>12.2f}%")
print(f"{'First year interest:':<22}${first_year_interest:>12.2f}")
