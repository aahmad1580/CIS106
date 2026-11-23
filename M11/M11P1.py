# M11P1 - Discount
def calculate_discount(quantity, price, discount_rate):
    subtotal = quantity * price
    discount_amount = subtotal * discount_rate / 100
    return discount_amount, subtotal - discount_amount


def main():
    quantity = int(input("Quantity: "))
    price = float(input("Unit price: "))
    discount_rate = float(input("Discount rate as a percent: "))
    discount_amount, discounted_price = calculate_discount(quantity, price, discount_rate)
    print(f"Quantity: {quantity}")
    print(f"Unit price: ${price:,.2f}")
    print(f"Discount amount: ${discount_amount:,.2f}")
    print(f"Discounted price: ${discounted_price:,.2f}")


if __name__ == "__main__":
    main()
