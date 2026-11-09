# M5P2 - Item Price
# Input: Item, quantity
# Processing: If item is A, unit price is $10; otherwise $20;
#             extended price = quantity * unit_price
# Output: Item, unit price, extended price

item = input("Enter the item (A or B): ")
quantity = int(input("Enter the quantity: "))

if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

extended_price = quantity * unit_price

print("Item:", item)
print(f"Unit price: ${unit_price:.2f}")
print(f"Extended price: ${extended_price:.2f}")
