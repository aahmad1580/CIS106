# M10P4 - Train Tickets
def ticket_price(miles):
    if miles >= 30:
        return 12
    if miles >= 20:
        return 10
    if miles >= 10:
        return 8
    return 5


total = 0
response = input("Do you want to enter data? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Last name: ")
    miles = float(input("Miles from downtown Chicago: "))
    price = ticket_price(miles)
    total += price
    print(f"{last_name} ticket price: ${price:.2f}")
    response = input("Enter another record? (Yes/No): ").strip().lower()

print(f"Total ticket sales: ${total:,.2f}")
