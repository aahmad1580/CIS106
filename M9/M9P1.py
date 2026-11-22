# M9P1 - Item Totals
# Assumption: the assignment's $10,0000.00 typo means $10,000.00.
def compute_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total *= 0.90
    return total


total_extended_price = 0.0
response = input("Do you want to enter an item? (Yes/No): ").strip().lower()
while response == "yes":
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per item: "))
    total = compute_total(quantity, price)
    total_extended_price += total
    print(f"Quantity: {quantity}")
    print(f"Price per item: ${price:,.2f}")
    print(f"Extended price after any discount: ${total:,.2f}")
    response = input("Do you want to enter another item? (Yes/No): ").strip().lower()

print(f"Total extended price: ${total_extended_price:,.2f}")
