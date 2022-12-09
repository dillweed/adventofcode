vertical_stacks = """    [H]         [D]     [P]        
[W] [B]         [C] [Z] [D]        
[T] [J]     [T] [J] [D] [J]        
[H] [Z]     [H] [H] [W] [S]     [M]
[P] [F] [R] [P] [Z] [F] [W]     [F]
[J] [V] [T] [N] [F] [G] [Z] [S] [S]
[C] [R] [P] [S] [V] [M] [V] [D] [Z]
[F] [G] [H] [Z] [N] [P] [M] [N] [D]
 1   2   3   4   5   6   7   8   9 """

print(vertical_stacks)

# Split layers by lines
layers = vertical_stacks.split("\n")
# Init main stack dictionary
horizontal_stacks = {}
# Init stack index helper dict
hor_stack_indexes = {}
# Iterate through layers starting from the bottom
for layer in layers[::-1]:
    for i, c in enumerate(layer):
        if i in hor_stack_indexes.keys():
            if c != " ":  # Do not add blanks
                horizontal_stacks[hor_stack_indexes[i]].append(c)
        if c.isdigit():
            horizontal_stacks[c] = []  # Main dict
            hor_stack_indexes[i] = c  # Track digit position in layer

print(horizontal_stacks, "\n", hor_stack_indexes)
