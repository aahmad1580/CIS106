# M4P4 - Calories Burned
# Input: First name, steps walked
# Processing: calories_burned = steps * 0.25
# Output: First name, calories burned

first_name = input("Enter your first name: ")
steps = int(input("Enter the number of steps walked today: "))

calories_burned = steps * 0.25

print("First name:", first_name)
print(f"Calories burned: {calories_burned:.2f}")
