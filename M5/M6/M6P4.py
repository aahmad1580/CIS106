# M6P4 - Concert Tickets
# Input: Number of tickets
# Processing: Choose price per ticket based on quantity;
#             total_cost = tickets * price_per_ticket
# Output: Number of tickets, price per ticket, total cost

tickets = int(input("Enter the number of tickets: "))

if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10:
    price_per_ticket = 60.00
elif tickets >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

total_cost = tickets * price_per_ticket

print(f"Number of tickets: {tickets}")
print(f"{'Price per ticket:':<22}${price_per_ticket:>12.2f}")
print(f"{'Total cost:':<22}${total_cost:>12.2f}")
