# M3P3 - Split Job Payment
# IPO Chart
# Input: Amount received
# Processing: amount_each = amount_received / 3
# Output: Amount each person receives

amount_received = float(input("Enter the amount received for the job: "))

amount_each = amount_received / 3

print(f"Each person receives: ${amount_each:.2f}")
