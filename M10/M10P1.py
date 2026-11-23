# M10P1 - Sales Forecast
def forecast_sales(month, sales):
    month = month.strip().lower()[:3]
    rates = {"jan": .10, "feb": .10, "mar": .10,
             "apr": .15, "may": .15, "jun": .15,
             "jul": .20, "aug": .20, "sep": .20,
             "oct": .25, "nov": .25, "dec": .25}
    return sales * (1 + rates[month])



response = input("Do you want to enter data? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Last name: ")
    month = input("Month: ")
    sales = float(input("Sales: "))
    print(f"{last_name} forecast: ${forecast_sales(month, sales):,.2f}")
    response = input("Enter another record? (Yes/No): ").strip().lower()


