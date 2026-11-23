# M10P2 - Room Paint
def wall_area(length, width, height):
    return 2 * (length + width) * height


def ceiling_or_floor_area(length, width):
    return length * width



response = input("Do you want to enter data? (Yes/No): ").strip().lower()
while response == "yes":
    length = float(input("Length in feet: "))
    width = float(input("Width in feet: "))
    height = float(input("Height in feet: "))
    print(f"Wall paint: {wall_area(length, width, height) / 50:.2f} gallons")
    print(f"Ceiling paint or floor varnish: {ceiling_or_floor_area(length, width) / 50:.2f} gallons")
    response = input("Enter another record? (Yes/No): ").strip().lower()


