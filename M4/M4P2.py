# M4P2 - Stock Value Change
# Input: Purchase price per share, current price, quantity
# Processing: value_change = (current_price - purchase_price) * quantity
# Output: Increase or decrease in stock value

purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = float(input("Enter the quantity of stock: "))

value_change = (current_price - purchase_price) * quantity

print(f"Change in stock value: ${value_change:.2f}")
