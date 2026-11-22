# M9P2 - Batting Averages
def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    return hits / at_bats


player_count = 0
response = input("Do you want to enter a player? (Yes/No): ").strip().lower()
while response == "yes":
    last_name = input("Enter the player's last name: ")
    hits = int(input("Enter the number of hits: "))
    at_bats = int(input("Enter the number of at bats: "))
    average = compute_batting_average(hits, at_bats)
    player_count += 1
    print(f"Last name: {last_name}")
    print(f"Batting average: {average:.3f}")
    response = input("Do you want to enter another player? (Yes/No): ").strip().lower()

print(f"Number of players: {player_count}")
