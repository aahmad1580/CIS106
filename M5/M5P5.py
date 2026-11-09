# M5P5 - Income Tax
# Input: Last name, number of dependents, gross income
# Processing: Adjusted income = gross income - dependents * 12000;
#             tax rate is 20% if adjusted income > $50000, otherwise 10%;
#             income tax = adjusted income * tax rate;
#             if income tax < 0, set it to $100
# Output: Last name, gross income, dependents, adjusted income, income tax

last_name = input("Enter your last name: ")
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter the gross income: "))

adjusted_income = gross_income - dependents * 12000

if adjusted_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adjusted_income * tax_rate

if income_tax < 0:
    income_tax = 100.00

print("Last name:", last_name)
print(f"Gross income: ${gross_income:.2f}")
print(f"Number of dependents: {dependents}")
print(f"Adjusted gross income: ${adjusted_income:.2f}")
print(f"Income tax: ${income_tax:.2f}")
