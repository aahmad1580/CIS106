# M11P4 - Bowling Averages
def calculate_bowling_averages(score1, score2, score3, handicap):
    average = (score1 + score2 + score3) / 3
    return average, average + handicap


def main():
    last_name = input("Bowler last name: ")
    score1 = float(input("First game score: "))
    score2 = float(input("Second game score: "))
    score3 = float(input("Third game score: "))
    handicap = float(input("Handicap per game: "))
    average, adjusted_average = calculate_bowling_averages(score1, score2, score3, handicap)
    print(f"Last name: {last_name}")
    print(f"Average score: {average:.2f}")
    print(f"Average score with handicap: {adjusted_average:.2f}")


if __name__ == "__main__":
    main()
