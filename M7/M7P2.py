# M7P2 - Number Sequence
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
increment = int(input("Enter the increment: "))

number = start
if increment == 0:
    print("The increment must be nonzero.")
else:
    while (increment > 0 and number <= stop) or (increment < 0 and number >= stop):
        print(number)
        number += increment
