with open("01_input.txt") as file:
    input_list = file.readlines()

elves = []
for line in input_list:
    try:
        elves[-1] += int(line)
    except:  # Line is empty
        elves.append(0)

print(max(elves))
# print(elves[-1]) # Test for final group
