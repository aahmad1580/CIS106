# M9P3 - Trip Miles Per Gallon
def compute_mpg(miles, gallons):
    return miles / gallons


trip_count = 0
response = input("Do you want to enter a trip? (Yes/No): ").strip().lower()
while response == "yes":
    destination = input("Enter the destination city: ")
    miles = float(input("Enter the miles travelled: "))
    gallons = float(input("Enter the gallons used: "))
    while gallons <= 0:
        gallons = float(input("Gallons must be greater than zero. Enter gallons used: "))
    mpg = compute_mpg(miles, gallons)
    trip_count += 1
    print(f"Destination city: {destination}")
    print(f"Miles travelled: {miles:,.2f}")
    print(f"Miles per gallon: {mpg:.2f}")
    response = input("Do you want to enter another trip? (Yes/No): ").strip().lower()

print(f"Number of trips: {trip_count}")
