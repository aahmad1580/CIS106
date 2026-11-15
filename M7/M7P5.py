# M7P5 - Order Discounts
total_discounts = 0.0
answer = input("Do you want to enter an order? (Yes/No): ")

while answer.strip().lower() == "yes":
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price per item: "))

    extended_price = round(quantity * price, 2)
    if extended_price > 10000.00:
        discount_rate = 0.25
    else:
        discount_rate = 0.10

    discount = extended_price * discount_rate
    total = extended_price - discount
    total_discounts += discount

    print(f"Extended price: ${extended_price:.2f}")
    print(f"Discount amount: ${discount:.2f}")
    print(f"Order total: ${total:.2f}")
    answer = input("Do you want to enter another order? (Yes/No): ")

print(f"Total discounts: ${total_discounts:.2f}")
