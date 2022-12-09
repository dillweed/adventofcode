# Read the input procedures file and store its lines in a list
with open("05_input_test.txt") as file:
    input_procedures = file.readlines()

# Read the input stacks file and store as a string
with open("05_input_stacks_test.txt") as file:
    vertical_stacks = file.read()


def main():
    print(vertical_stacks)
    stacks: dict[str, list[str]] = transpose_stacks(vertical_stacks)
    print(stacks)
    procedures: list[list[int]] = parse_procedures(input_procedures)
    print(procedures)


def transpose_stacks(vertical_stacks):
    # Split layers by lines
    layers = vertical_stacks.split("\n")
    # Init horizontal stack dictionary
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

    return horizontal_stacks


def parse_procedures(input_procedures: list[str]) -> list[list[int]]:
    procedures = []
    for line in input_procedures:
        procedures.append([int(s) for s in line.split() if s.isdigit()])
    return procedures


if __name__ == "__main__":
    main()
