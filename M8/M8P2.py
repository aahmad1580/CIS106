# M8P2 - Fibonacci Sequence
first = 1
second = 1

for count in range(20):
    print(first)
    next_number = first + second
    first = second
    second = next_number
