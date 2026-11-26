# M12P1 - Arrays

def display_names(names):
    for index in range(len(names)):
        print(names[index])


def display_reverse(names):
    for index in range(len(names) - 1, -1, -1):
        print(names[index])


names = ['Ahmad', 'Lee', 'Khan', 'Garcia', 'Patel', 'Chen', 'Brown', 'Davis', 'Nguyen', 'Wilson']

print("Original order")
display_names(names)
print("\nReverse order")
display_reverse(names)
