with open("03_input.txt") as file:
    input_list = file.readlines()

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

unique_items = []
priority_dict = 

for line in input_list:
    for _c in line[:len(line)/2]:
        if _c in line[len(line)/2:]:
