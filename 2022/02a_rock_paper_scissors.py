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

# Create a translation table to replace X, Y, and Z with the possible choices
trans_dict = str.maketrans("XYZ", "".join(CHOICES))


def calculate_winner(oppo, mine):
    global my_score, oppo_score
    # Check if the opponent won
    if (CHOICES.index(oppo) - CHOICES.index(mine)) % 3 == 1:
        # Update the scores
        my_score += CHOICES.index(mine) + 1
        oppo_score += CHOICES.index(oppo) + 1
        oppo_score += win_score
        # Print the updated scores
        print(f"Adding {CHOICES.index(mine) + 1} to my_score {my_score}")
        print(
            f"Adding {CHOICES.index(oppo) + 1} and {win_score} to oppo_score {oppo_score}"
        )
        # Return the result
        return "Opponent wins!\n"
    # Check if the player won
    elif (CHOICES.index(oppo) - CHOICES.index(mine)) % 3 == 2:
        # Update the scores
        my_score += CHOICES.index(mine) + 1
        oppo_score += CHOICES.index(oppo) + 1
        my_score += win_score
        # Print the updated scores
        print(
            f"Adding {CHOICES.index(mine) + 1} and {win_score} to my_score {my_score}"
        )
        print(f"Adding {CHOICES.index(oppo) + 1} to oppo_score {oppo_score}")
        # Return the result
        return "I win!\n"
    # If it is a tie
    else:
        # Update the scores
        my_score += CHOICES.index(mine) + 1
        oppo_score += CHOICES.index(oppo) + 1
        my_score += tie_score
        oppo_score += tie_score
        # Print the updated scores
        print(
            f"Adding {CHOICES.index(mine) + 1} and {tie_score} to my_score {my_score}"
        )
        print(
            f"Adding {CHOICES.index(oppo) + 1} and {tie_score} to oppo_score {oppo_score}"
        )
        # Return the result
        return "It's a tie!\n"


# Iterate over the lines in the input list
for line in input_list:
    # Split the line into the opponent's and player's choices
    oppo, mine = line.split()
    # Format the input by replacing X, Y, and Z with the possible choices
    formatted_input_list = (oppo, mine.translate(trans_dict))
    # Calculate the winner and print the result
    print(calculate_winner(oppo, mine.translate(trans_dict)))

# Print the final scores
print(f"my_score: {my_score}")
print(f"oppo_score: {oppo_score}")
