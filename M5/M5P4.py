# M5P4 - Appliance Warranty
# Input: Appliance name, cost
# Processing: Warranty is 10% if cost > $1000, otherwise 5%;
#             total = cost + warranty
# Output: Appliance name, cost, warranty cost, total

appliance = input("Enter the appliance name: ")
cost = float(input("Enter the appliance cost: "))

if cost > 1000.00:
    warranty = cost * 0.10
else:
    warranty = cost * 0.05

total = cost + warranty

print("Appliance:", appliance)
print(f"Appliance cost: ${cost:.2f}")
print(f"Warranty cost: ${warranty:.2f}")
print(f"Total: ${total:.2f}")
