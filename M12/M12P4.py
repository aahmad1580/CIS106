# M12P4 - Arrays

from pathlib import Path


def load_data():
    names = []
    values = []
    data_path = Path(__file__).with_name("M12_Players.txt")
    with data_path.open(encoding="utf-8") as data_file:
        for line in data_file:
            name, value = line.strip().split(",")
            names.append(name)
            values.append(float(value))
    return names, values


def display_players(names, averages):
    print("Last name  Batting average")
    for index in range(len(names)):
        print(f"{names[index]:<11}{averages[index]:.3f}")


def search_player(names, averages, last_name):
    for index in range(len(names)):
        if names[index].lower() == last_name.lower():
            print(f"{names[index]}: {averages[index]:.3f}")
            return


names, averages = load_data()
display_players(names, averages)
last_name = input("Enter a last name (or press Enter to stop): ").strip()
while last_name:
    search_player(names, averages, last_name)
    last_name = input("Enter a last name (or press Enter to stop): ").strip()
