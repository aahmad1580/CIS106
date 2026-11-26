# M12P3 - Arrays

from pathlib import Path


def load_data():
    names = []
    values = []
    data_path = Path(__file__).with_name("M12_Students.txt")
    with data_path.open(encoding="utf-8") as data_file:
        for line in data_file:
            name, value = line.strip().split(",")
            names.append(name)
            values.append(int(value))
    return names, values


def display_high_and_low(names, scores):
    high_index = 0
    low_index = 0
    for index in range(1, len(scores)):
        if scores[index] > scores[high_index]:
            high_index = index
        if scores[index] < scores[low_index]:
            low_index = index
    print(f"Highest score: {names[high_index]} {scores[high_index]}")
    print(f"Lowest score: {names[low_index]} {scores[low_index]}")


names, scores = load_data()
display_high_and_low(names, scores)
