# M3P1 - Stock Investment
# IPO Chart
# Input: Stock ticker, number of shares, cost per share
# Processing: amount_invested = shares * cost_per_share
# Output: Stock ticker, amount invested

ticker = input("Enter the stock ticker symbol: ")
shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

amount_invested = shares * cost_per_share

print("Stock ticker:", ticker)
print(f"Amount invested: ${amount_invested:.2f}")
