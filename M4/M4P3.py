# M4P3 - Meal Tips
# Input: Meal total
# Processing: Multiply meal total by 0.15, 0.18, and 0.20; add each tip to meal total
# Output: Meal total, tip, total with tip for each rate

meal_total = float(input("Enter the total for the meal: "))

tip15 = meal_total * 0.15
tip18 = meal_total * 0.18
tip20 = meal_total * 0.20

total15 = meal_total + tip15
total18 = meal_total + tip18
total20 = meal_total + tip20

print()
print("With 15% Tip:")
print()
print(f"{'Total:':<16}{meal_total:>10.2f}")
print(f"{'Tip:':<16}{tip15:>10.2f}")
print(f"{'Total with Tip':<16}{total15:>10.2f}")
print()
print("With 18% Tip:")
print()
print(f"{'Total:':<16}{meal_total:>10.2f}")
print(f"{'Tip:':<16}{tip18:>10.2f}")
print(f"{'Total with Tip':<16}{total18:>10.2f}")
print()
print("With 20% Tip:")
print()
print(f"{'Total:':<16}{meal_total:>10.2f}")
print(f"{'Tip:':<16}{tip20:>10.2f}")
print(f"{'Total with Tip':<16}{total20:>10.2f}")
