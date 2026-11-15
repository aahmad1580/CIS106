# M8P1 - Five Years of Compound Interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

balance = principal

print()
print(f"{'Year':>4} {'Beginning':>16} {'Ending':>16}")
print(f"{'':>4} {'Balance':>16} {'Balance':>16}")
print()

for year in range(1, 6):
    beginning_balance = balance
    interest = beginning_balance * rate
    balance = beginning_balance + interest

    beginning_display = f"${beginning_balance:,.2f}"
    ending_display = f"${balance:,.2f}"
    print(f"{year:>4} {beginning_display:>16} {ending_display:>16}")

total_interest = balance - principal
print(f"\nTotal interest earned: ${total_interest:,.2f}")
