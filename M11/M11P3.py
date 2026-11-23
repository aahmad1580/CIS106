# M11P3 - Sales Report
def calculate_sales_report(sales):
    if sales > 100000:
        commission_rate = 0.10
    else:
        commission_rate = 0.05
    commission = sales * commission_rate
    next_year_target = sales * 0.05
    return commission, next_year_target


def main():
    last_name = input("Salesperson last name: ")
    sales = float(input("Sales: "))
    commission, next_year_target = calculate_sales_report(sales)
    print(f"Last name: {last_name}")
    print(f"Commission: ${commission:,.2f}")
    print(f"Next year's target: ${next_year_target:,.2f}")


if __name__ == "__main__":
    main()
