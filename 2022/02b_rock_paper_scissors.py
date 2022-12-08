# Open the input file and read its lines into a list
with open("02_input.txt") as file:
    input_list = file.readlines()

# Initialize variables to store the scores of the player and the opponent
my_score = 0
oppo_score = 0

# Set the number of points awarded for a win and a tie
win_score = 6
tie_score = 3

# Create an empty list to store the formatted input
formatted_input_list = []

# Define the possible choices
CHOICES = ["A", "B", "C"]

# Define the relationship between the plays and the result
PLAYS = {"X": "lose", "Y": "tie", "Z": "win"}

# Define the verbose names of the choices
VERBOSE = {"A": "Rock", "B": "Paper", "C": "Scissors"}


# Define a function to calculate the winner of a game
def calculate_winner(oppo_pick, my_pick):
    global my_score, oppo_score
    # Check if the opponent won
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
    # Check if the player won
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
    # If it is a tie
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


# Calculate the outcome of a round according to the play
def process_input(oppo_pick, my_play):
    if PLAYS[my_play] == "lose":
        my_pick = CHOICES[(CHOICES.index(oppo_pick) + 2) % 3]
    if PLAYS[my_play] == "tie":
        my_pick = oppo_pick
    if PLAYS[my_play] == "win":
        my_pick = CHOICES[(CHOICES.index(oppo_pick) + 1) % 3]
    return calculate_winner(oppo_pick, my_pick)


# Iterate over the lines in the input list
for line in input_list:
    # Split the line into the opponent's and player's choices
    oppo_pick, my_play = line.split()
    print(process_input(oppo_pick, my_play))

# Print the final scores
print(f"my_score: {my_score}")
print(f"oppo_score: {oppo_score}")
