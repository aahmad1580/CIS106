# M12P2 - Arrays

def display_names(names, scores):
    for index in range(len(names)):
        print(names[index], scores[index])


def display_reverse(names, scores):
    for index in range(len(names) - 1, -1, -1):
        print(names[index], scores[index])


names = ['Ahmad', 'Lee', 'Khan', 'Garcia', 'Patel', 'Chen', 'Brown', 'Davis', 'Nguyen', 'Wilson']
scores = [88, 92, 79, 85, 98, 90, 72, 83, 95, 87]

print("Original order")
display_names(names, scores)
print("\nReverse order")
display_reverse(names, scores)
