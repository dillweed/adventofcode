# Read the input procedures file and store its lines in a list
with open("05_input.txt") as file:
    input_procedures = file.readlines()

# Read the input stacks file and store as a string
with open("05_input_stacks.txt") as file:
    vertical_stacks = file.read()


def main():
    print("Initial stack string: \n", vertical_stacks, sep="")
    stacks = transpose_stacks(vertical_stacks)
    print("Transposed stacks: \n", stacks)
    procedures = parse_procedures(input_procedures)
    print("Procedures: \n", procedures)
    stacks_after_move = move_stacks(stacks, procedures)
    print("Stacks after move: \n", stacks_after_move)
    top_crates = get_top_crates(stacks_after_move)
    print("Top crates: \n", top_crates)


def transpose_stacks(vertical_stacks: str) -> dict[int, list[str]]:
    # Split layers by lines
    layers = vertical_stacks.split("\n")
    # Init horizontal stack dictionary
    horizontal_stacks: dict[int, list[str]] = {}
    # Init stack index helper dict
    column_indexes: dict[int, int] = {}
    # Iterate through layers starting from the bottom
    for layer in layers[::-1]:
        for i, c in enumerate(layer):
            if i in column_indexes.keys():
                if c != " ":  # Do not add blanks
                    horizontal_stacks[column_indexes[i]].append(c)
            if c.isdigit():
                horizontal_stacks[int(c)] = []  # Init dict key for a stack
                column_indexes[i] = int(c)  # Track column positions in layer
    return horizontal_stacks


def parse_procedures(input_procedures: list[str]) -> list[list[int]]:
    procedures = []
    for line in input_procedures:
        procedures.append([int(s) for s in line.split() if s.isdigit()])
    return procedures


def move_stacks(stacks, procedures) -> dict[int, list[str]]:
    """Process procedures on stacks.
    Example list item in procedures: [21, 3, 7]
    Move 21 crates from stack 3 to stack 7.
    Each move pops from the end of the stack. LIFO

    Args:
        stacks (dict): stacks of crates in initial position
        procedures (list): Orders to move n crates from stack n to stack n

    Returns:
        dict: Position of crates in stacks after moving
    """
    for procedure in procedures:
        for i in range(procedure[0]):
            stacks[procedure[2]].append(stacks[procedure[1]].pop())
    return stacks


def get_top_crates(stacks_after_move) -> str:
    top_crates = ""
    for key, value in stacks_after_move.items():
        top_crates += value[-1]
    return top_crates


if __name__ == "__main__":
    main()
