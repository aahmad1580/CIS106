# M11P5 - Item Total and Tax
total = 0.0
tax = 0.0


def calculate_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * 0.07


def main():
    quantity = int(input("Quantity: "))
    unit_price = float(input("Unit price: "))
    calculate_total_and_tax(quantity, unit_price)
    print(f"Total before tax: ${total:,.2f}")
    print(f"Tax: ${tax:,.2f}")


if __name__ == "__main__":
    main()
