# Opponent: A for rock, B paper, C scissors.
# You: X for rock, Y paper, Z scissors.

# Total score is the sum of the scores for each round.

# PART 1:
# The score for a single round is the score for the shape you selected:
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# PART 2:
# The letters mean you need to -> X: LOSE Y: DRAW Z: WIN

cases = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}

cases_part_2 = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}


def day2():
    total_score = 0

    with open("input_day2", "r") as file:
        lines = file.readlines()
    for line in lines:
        opponent = line.split(' ')[0]
        you = (line.split(' ')[1])[:-1]
        round_case = opponent + you
        total_score = total_score + cases_part_2[round_case]
    print("Your total score is: " + str(total_score))


if __name__ == "__main__":
    day2()
