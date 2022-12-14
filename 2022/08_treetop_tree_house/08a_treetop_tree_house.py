"""TBA."""


def main():
    """TBA."""
    # Define input filename
    input_file = "08_input.txt"
    # Load input string as 2d array
    trees = load_input_file(input_file)
    [print(*row) for row in trees]
    hidden = num_hidden(trees)
    # I accidentally wrote this for hidden trees, not visible.
    total_trees = sum([len(row) for row in trees])
    print("Number of visible trees:", total_trees - hidden)


def num_hidden(trees) -> int:
    hidden = 0
    tree_dict = {}

    # Check horizontal tree visibility
    for i, row in enumerate(trees):
        if i == 0 or i == len(trees) - 1:  # Skip edge rows
            print("edge row:", row)
            continue
        for j in range(1, len(row) - 1):
            print("row:", row, ", item:", row[j], ", i:", i, ", j:", j)
            # Assign boolean result in list as value to i,j coordinate key
            tree_dict[i, j] = [row[j] <= max(row[:j]) and row[j] <= max(row[j + 1 :])]
            print(row[j], row, tree_dict[i, j])

    # Check vertical tree visibility
    for col_index in range(1, len(trees[0]) - 1):  # Skip edge columns
        col = []  # Individual column
        for i, row in enumerate(trees):
            col.append(row[col_index])
        print(col)
        for i in range(1, len(col) - 1):  # Skip column ends
            # Append boolean result to list value of i,col_index coordinate key
            tree_dict[i, col_index].append(
                col[i] <= max(col[:i]) and col[i] <= max(col[i + 1 :])
            )
            print("col i:", col[i], tree_dict[i, col_index])

    print(tree_dict)
    # Count "True, True" pairs from coordinate dict
    hidden = sum([i and j for i, j in tree_dict.values()])
    return hidden


def load_input_file(input_file) -> list[list[int]]:
    with open(input_file) as file:
        trees_str = file.read()

    trees: list[list] = [[] for _ in range(len(trees_str.split("\n")))]

    for i, line in enumerate(trees_str.split("\n")):
        for j, c in enumerate(line):
            trees[i].append(int(c))

    return trees


if __name__ == "__main__":
    main()
