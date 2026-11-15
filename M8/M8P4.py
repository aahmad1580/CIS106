# M8P4 - Order Totals
from pathlib import Path

data_file = Path(__file__).with_name("M8P4_Orders.txt")
total_sales = 0.0
order_count = 0

print(f"{'Item':<16}{'Quantity':>10}{'Price':>12}{'Extended Price':>18}")

with data_file.open(encoding="utf-8") as orders:
    for line in orders:
        item = line.strip()
        quantity = int(orders.readline())
        price = float(orders.readline())

        extended_price = quantity * price
        total_sales += extended_price
        order_count += 1

        price_display = f"${price:,.2f}"
        extended_display = f"${extended_price:,.2f}"
        print(f"{item:<16}{quantity:>10}{price_display:>12}{extended_display:>18}")

average_order = 0.0
if order_count > 0:
    average_order = total_sales / order_count

print(f"\nTotal of extended prices: ${total_sales:,.2f}")
print(f"Number of orders: {order_count}")
print(f"Average order: ${average_order:,.2f}")
