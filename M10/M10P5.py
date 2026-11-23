# M10P5 - Home Assessment
def assess_home(county, market_value):
    rates = {"cook": .90, "dupage": .80, "mchenry": .75, "kane": .60}
    return market_value * rates.get(county.strip().lower(), .70)


total_market = 0.0
total_assessed = 0.0
response = input("Do you want to enter data? (Yes/No): ").strip().lower()
while response == "yes":
    county = input("County: ")
    market_value = float(input("Market value: "))
    assessed_value = assess_home(county, market_value)
    total_market += market_value
    total_assessed += assessed_value
    print(f"Assessed value: ${assessed_value:,.2f}")
    response = input("Enter another record? (Yes/No): ").strip().lower()

print(f"Total market value: ${total_market:,.2f}")
print(f"Total assessed value: ${total_assessed:,.2f}")
