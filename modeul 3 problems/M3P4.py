# M3P4 - Auto Discount
# IPO Chart
# Input: Make, model, MSRP, discount as a decimal
# Processing: amount_off = msrp * discount_percent; discounted_price = msrp - amount_off
# Output: Make, model, MSRP, discount percent, amount off, discounted price

make = input("Enter the auto make: ")
model = input("Enter the auto model: ")
msrp = float(input("Enter the MSRP: "))
discount_percent = float(input("Enter the discount as a decimal (0.10 for 10%): "))

amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

print("Make:", make)
print("Model:", model)
print(f"MSRP: ${msrp:.2f}")
print(f"Discount percent: {discount_percent:.2%}")
print(f"Amount off: ${amount_off:.2f}")
print(f"Discounted price: ${discounted_price:.2f}")
