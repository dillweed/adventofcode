with open("02_input.txt") as file:
    input_list = file.readlines()

my_score = 0
oppo_score = 0
win_score = 6
tie_score = 3
formatted_input_list = []
processed_play_list = []
CHOICES = ["A", "B", "C"]
PLAYS = {"X": "lose", "Y": "tie", "Z": "win"}
VERBOSE = {"A": "Rock", "B": "Paper", "C": "Scissors"}


def calculate_winner(oppo_pick, my_pick):
    global my_score, oppo_score
    if (CHOICES.index(oppo_pick) - CHOICES.index(my_pick)) % 3 == 1:
        my_score += CHOICES.index(my_pick) + 1
        oppo_score += CHOICES.index(oppo_pick) + 1
        oppo_score += win_score
        print(f"oppo_pick: {VERBOSE[oppo_pick]}")
        print(f"my_pick: {VERBOSE[my_pick]}")
        print(f"Adding {CHOICES.index(my_pick) + 1} to my_score {my_score}")
        print(
            f"Adding {CHOICES.index(oppo_pick) + 1} and {win_score} to oppo_score {oppo_score}"
        )
        return "Opponent wins!\n"
    elif (CHOICES.index(oppo_pick) - CHOICES.index(my_pick)) % 3 == 2:
        my_score += CHOICES.index(my_pick) + 1
        oppo_score += CHOICES.index(oppo_pick) + 1
        my_score += win_score
        print(f"oppo_pick: {VERBOSE[oppo_pick]}")
        print(f"my_pick: {VERBOSE[my_pick]}")
        print(
            f"Adding {CHOICES.index(my_pick) + 1} and {win_score} to my_score {my_score}"
        )
        print(f"Adding {CHOICES.index(oppo_pick) + 1} to oppo_score {oppo_score}")
        return "I win!\n"
    else:
        my_score += CHOICES.index(my_pick) + 1
        oppo_score += CHOICES.index(oppo_pick) + 1
        my_score += tie_score
        oppo_score += tie_score
        print(f"oppo_pick: {VERBOSE[oppo_pick]}")
        print(f"my_pick: {VERBOSE[my_pick]}")
        print(
            f"Adding {CHOICES.index(my_pick) + 1} and {tie_score} to my_score {my_score}"
        )
        print(
            f"Adding {CHOICES.index(oppo_pick) + 1} and {tie_score} to oppo_score {oppo_score}"
        )
        return "It's a tie!\n"


def process_input(oppo_pick, my_play):
    if PLAYS[my_play] == "lose":
        my_pick = CHOICES[(CHOICES.index(oppo_pick) + 2) % 3]
    if PLAYS[my_play] == "tie":
        my_pick = oppo_pick
    if PLAYS[my_play] == "win":
        my_pick = CHOICES[(CHOICES.index(oppo_pick) + 1) % 3]
    return calculate_winner(oppo_pick, my_pick)


for line in input_list:
    oppo_pick, my_play = line.split()
    print(process_input(oppo_pick, my_play))


print(f"my_score: {my_score}")
print(f"oppo_score: {oppo_score}")
