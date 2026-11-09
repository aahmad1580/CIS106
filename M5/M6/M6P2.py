# M6P2 - Part Cost
# Input: Part number, quantity
# Processing: Choose unit cost based on part number;
#             total_cost = quantity * unit_cost
# Output: Part number, cost per unit, total cost

part_number = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))

if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

print("Part number:", part_number)
print(f"{'Cost per unit:':<22}${unit_cost:>12.2f}")
print(f"{'Total cost:':<22}${total_cost:>12.2f}")
