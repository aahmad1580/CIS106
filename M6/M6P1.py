# M6P1 - Widget Total
# Input: Quantity of widgets
# Processing: Choose unit price; extended price = quantity * unit_price;
#             tax = extended_price * 0.07; total = extended_price + tax
# Output: Extended price, tax, total

quantity = int(input("Enter the quantity of widgets: "))

if quantity > 10000:
    unit_price = 10.00
elif quantity >= 5000:
    unit_price = 20.00
else:
    unit_price = 30.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

print(f"{'Extended price:':<22}${extended_price:>12.2f}")
print(f"{'Tax:':<22}${tax:>12.2f}")
print(f"{'Total:':<22}${total:>12.2f}")
