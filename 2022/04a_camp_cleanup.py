# Read the input file and store its lines in a list
with open("04_input.txt") as file:
    input_list = file.readlines()

full_overlaps = 0

for item in input_list:
    a, b = item.split(",")
    firstolomew = [int(n.strip()) for n in a.split("-")]
    secundus = [int(n.strip()) for n in b.split("-")]
    if (firstolomew[0] <= secundus[0] and firstolomew[1] >= secundus[1]) or (
        secundus[0] <= firstolomew[0] and secundus[1] >= firstolomew[1]
    ):
        full_overlaps += 1

print(full_overlaps)
