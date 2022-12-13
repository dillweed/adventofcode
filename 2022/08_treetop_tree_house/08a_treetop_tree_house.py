"""TBA."""


def main():
    """TBA."""
    # Define input filename
    input_file = "08_input_test.txt"
    # Load input string as 2d array
    trees = load_input_file(input_file)

    [print(*row) for row in trees]
    print("row2 reversed:", trees[1][::-1])
    print("col2 reversed:", [row[1] for row in trees][::-1])


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
