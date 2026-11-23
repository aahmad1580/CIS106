# M11P2 - Exam Scores
def calculate_exam_results(score1, score2, score3):
    total_points = score1 + score2 + score3
    return total_points, total_points / 3


def main():
    last_name = input("Student last name: ")
    score1 = float(input("First exam score: "))
    score2 = float(input("Second exam score: "))
    score3 = float(input("Third exam score: "))
    total_points, average = calculate_exam_results(score1, score2, score3)
    print(f"Last name: {last_name}")
    print(f"Total points: {total_points:.2f}")
    print(f"Average exam score: {average:.2f}")


if __name__ == "__main__":
    main()
