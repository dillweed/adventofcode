# Read the input file and store its lines in a list
with open("04_input.txt") as file:
    input_list = file.readlines()

partial_overlaps = 0

for item in input_list:
    a, b = item.split(",")
    firstolomew = [int(n.strip()) for n in a.split("-")]
    secundus = [int(n.strip()) for n in b.split("-")]
    found = False
    for n in range(firstolomew[0], firstolomew[1] + 1):
        if found:
            break
        if n in range(secundus[0], secundus[1] + 1):
            found = True
            partial_overlaps += 1

print(partial_overlaps)
