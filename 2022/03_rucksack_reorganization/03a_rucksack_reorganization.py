import re

# Read the input file and store its lines in a list
with open("03_input.txt") as file:
    input_list = file.readlines()


def replace_letters_with_numbers(text):
    # Define the pattern to match letters
    pattern = r"[a-zA-Z]"

    # Replace the matched letters with their corresponding numbers
    return re.sub(
        pattern,
        lambda m: str(
            ord(m.group(0).lower()) - ord("a") + 1 + (26 if m.group(0).isupper() else 0)
        ),
        text,
    )


# Initialize the priority sum
priority_sum = 0

# Iterate over the lines in the input list
for line in input_list:
    # Find the middle index of the line
    middle = len(line) // 2

    # Initialize a flag to track if the current character has been found in the second half of the line
    found = False

    # Iterate over the first half of the line
    for _c in line[:middle]:
        if found:
            break

        # Check if the current character is in the second half of the line
        if _c in line[middle:]:
            found = True
            # If it is, add its corresponding number to the priority sum
            priority_sum += int(replace_letters_with_numbers(_c))

# Print the final priority sum
print(priority_sum)
