# Open the input file and read its lines into a list
with open("01_input.txt") as file:
    input_list = file.readlines()

# Initialize a list to store the total number of calories each elf has
elves = []

# Iterate over the lines in the input list
for line in input_list:
    # Try to add the number of calories from the current line to the last element in the elves list
    try:
        elves[-1] += int(line)
    except:
        # If the line is empty or an error occurs, add a new element to the list with a value of 0
        elves.append(0)

# Print the maximum number of calories from the elves list
print(max(elves))
