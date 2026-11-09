# M5P3 - Book Shipping
# Input: Number of books, cost per book
# Processing: Order total = books * cost_per_book;
#             shipping is $0 if total > $50, otherwise $25
# Output: Order total, shipping charge

books = int(input("Enter the number of books: "))
cost_per_book = float(input("Enter the cost per book: "))

order_total = books * cost_per_book

if order_total > 50.00:
    shipping = 0.00
else:
    shipping = 25.00

print(f"Order total: ${order_total:.2f}")
print(f"Shipping charge: ${shipping:.2f}")
