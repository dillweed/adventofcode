# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you
# selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus
# the score for the outcome of the round (0 if you lost, 3 if
# the round was a draw, and 6 if you won).

# A or X for Rock, B or Y for Paper, and C or Z for Scissors

# Compare against map of possible outcomes and apply a score.
# What are the outcomes and how might they be mapped efficiently?
# Look at previous RPS exercise for modulo algo.

with open("02_input.txt") as file:
    input_list = file.readlines()

my_score = 0
oppo_score = 0
win_score = 6
tie_score = 3
formatted_input_list = []
CHOICES = ["A", "B", "C"]
trans_dict = str.maketrans("XYZ", "".join(CHOICES))


def calculate_winner(oppo, mine):
    global my_score, oppo_score
    if (CHOICES.index(oppo) - CHOICES.index(mine)) % 3 == 1:
        my_score += CHOICES.index(mine) + 1
        oppo_score += CHOICES.index(oppo) + 1
        oppo_score += win_score
        print(f"Adding {CHOICES.index(mine) + 1} to my_score {my_score}")
        print(
            f"Adding {CHOICES.index(oppo) + 1} and {win_score} to oppo_score {oppo_score}"
        )
        return "Opponent wins!\n"
    elif (CHOICES.index(oppo) - CHOICES.index(mine)) % 3 == 2:
        my_score += CHOICES.index(mine) + 1
        oppo_score += CHOICES.index(oppo) + 1
        my_score += win_score
        print(
            f"Adding {CHOICES.index(mine) + 1} and {win_score} to my_score {my_score}"
        )
        print(f"Adding {CHOICES.index(oppo) + 1} to oppo_score {oppo_score}")
        return "I win!\n"
    else:
        my_score += CHOICES.index(mine) + 1
        oppo_score += CHOICES.index(oppo) + 1
        my_score += tie_score
        oppo_score += tie_score
        print(
            f"Adding {CHOICES.index(mine) + 1} and {tie_score} to my_score {my_score}"
        )
        print(
            f"Adding {CHOICES.index(oppo) + 1} and {tie_score} to oppo_score {oppo_score}"
        )
        return "It's a tie!\n"


for line in input_list:
    oppo, mine = line.split()
    formatted_input_list = (oppo, mine.translate(trans_dict))
    print(calculate_winner(oppo, mine.translate(trans_dict)))

print(f"my_score: {my_score}")
print(f"oppo_score: {oppo_score}")
