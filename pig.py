import random

def roll():
    min_value = 1
    max_value = 6
    roll= random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter a number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2 - 4 players.")

    else:
        print("Invalid, please try again")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

    for players_idx in range(players):

        print("\nPlayer number", players_idx + 1, "turn has just started!")
        print("Your total score is:", players_scores[players_idx], "\n")
        current_score = 0

        while True:
            should_roll= input("Would you like to roll (y)?: ")
            if should_roll.lower() != "y":
                break
            value=roll()
            if value == 1:
                print("You rolled a 1! Turn done !!!")
                current_score=0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
                print(f"Your score is : {current_score}")
    players_scores[players_idx] += current_score
    print(f"Your total score is: {players_scores[players_idx]}")


max_score=max(players_scores)
winning_idx = players_scores.index(max_score)
print(f"Player number {winning_idx + 11} si the winner with a score of : {max}")