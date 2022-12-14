from functools import reduce

"""TBA."""


def main():
    """TBA."""
    # Define input filename
    input_file = "08_input.txt"
    # Load input string as 2d array
    trees = load_input_file(input_file)
    [print(*row) for row in trees]
    high_score = score(trees)

    print("Highest score tree:", high_score)


def score(trees) -> int:
    high_score = 0
    tree_dict: dict[tuple[int, int], list[int]] = {}

    # Check horizontal tree visibility
    for i, row in enumerate(trees):
        for j in range(len(row)):
            try:
                tree_dict[i, j]
            except:
                tree_dict[i, j] = []  # Init key with empty list
                print("adding [] for", i, j)
            print("calling forward for", i, j)
            tree_dict[i, j].append(view_distance_forward(j, row))
            print("calling behind for", i, j)
            tree_dict[i, j].append(view_distance_behind(j, row))
            print("row i:", i, "row n:", row[j], row, tree_dict[i, j], "\n")

    # Check vertical tree visibility
    for col_index in range(len(trees[0])):
        col = []  # Individual column
        for i, row in enumerate(trees):
            col.append(row[col_index])
        for i in range(len(col)):
            tree_dict[i, col_index].append(view_distance_forward(i, col))
            tree_dict[i, col_index].append(view_distance_behind(i, col))
            print("col i:", i, "col n:", col[i], col, tree_dict[i, col_index], "\n")

    print(tree_dict)
    scores = [reduce((lambda x, y: x * y), tree) for tree in tree_dict.values()]
    print(scores)
    high_score = max(scores)
    return high_score


def view_distance_forward(house_i, line) -> int:
    distance = 0
    offset = -1
    print("forward called with", house_i, line)
    for view_i in range(house_i + 1, len(line)):
        print(
            "subloop forward",
            "house n:",
            line[house_i],
            "view_i:",
            view_i,
            "view n:",
            line[view_i],
        )
        if line[view_i] >= line[house_i]:
            offset = view_i - house_i
            print("offset", offset)
            break
    if offset == -1:  # no trees >= found
        distance = len(line) - 1 - house_i
    else:
        distance = offset
    print("returning distance:", distance)
    return distance


def view_distance_behind(house_i, line) -> int:
    distance = 0
    offset = -1
    print("behind called with", house_i, line)
    for view_i in range(house_i - 1, -1, -1):
        print(
            "subloop behind",
            "house n:",
            line[house_i],
            "view_i:",
            view_i,
            "view n:",
            line[view_i],
        )
        if line[view_i] >= line[house_i]:
            offset = house_i - view_i
            print("offset", offset)
            break
    if offset == -1:  # no trees >= found
        distance = house_i
    else:
        distance = offset
    print("returning distance:", distance)
    return distance


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
