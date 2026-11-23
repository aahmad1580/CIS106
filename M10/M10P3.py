# M10P3 - Vehicle Prices
def out_the_door_price(msrp, make, model, electric_code):
    make = make.strip().lower()
    model = model.strip().lower().replace("-", "").replace(" ", "")
    # Apply the electric rate first because it covers all electric vehicles.
    if electric_code.strip().upper() == "Y":
        rate = .30
    elif (make, model) == ("honda", "accord"):
        rate = .10
    elif (make, model) == ("toyota", "rav4"):
        rate = .15
    else:
        rate = .05
    return msrp * (1 - rate) * 1.07


total_msrp = 0.0
total_sales = 0.0
response = input("Do you want to enter data? (Yes/No): ").strip().lower()
while response == "yes":
    make = input("Make: ")
    model = input("Model: ")
    electric_code = input("Electric vehicle (Y/N): ")
    msrp = float(input("MSRP: "))
    price = out_the_door_price(msrp, make, model, electric_code)
    total_msrp += msrp
    total_sales += price
    print(f"Out-the-door price: ${price:,.2f}")
    response = input("Enter another record? (Yes/No): ").strip().lower()

print(f"Total MSRP: ${total_msrp:,.2f}")
print(f"Total sales price: ${total_sales:,.2f}")
