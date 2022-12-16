import inspect
from dataclasses import dataclass, asdict, astuple, field
from pprint import pprint
from collections import defaultdict


@dataclass(frozen=True, order=True)
class Tree:
    x_i: int
    y_i: int
    height: int
    list_i: int
    things: list[int] = field(default_factory=list)
    visible: bool = field(default=False)

    def set_visible(self):
        object.__setattr__(self, "visible", True)


def load_input_file(input_file) -> list[list[int]]:
    with open(input_file) as file:
        trees_str = file.read()

    trees_list: list[list] = [[] for _ in range(len(trees_str.split("\n")))]

    for i, line in enumerate(trees_str.split("\n")):
        for j, c in enumerate(line):
            trees_list[i].append(int(c))

    return trees_list


def main():
    input_file = "08_input_test.txt"
    trees_list = load_input_file(input_file)
    forest = defaultdict(lambda: "Not in the forest")
    for y, line in enumerate(trees_list):
        for x, height in enumerate(line):
            this_tree = Tree(x, y, height, list_i=len(forest))
            forest[x, y] = this_tree

    pprint(inspect.getmembers(Tree, inspect.isfunction))

    # Change attributes after instantiation
    forest[3, 2].things.append("aoeu")
    forest[3, 2].things.append(234)
    forest[3, 2].set_visible()
    print("Updated tree:", forest[3, 2])

    print(
        "Compare heights using absolute coordinates",
        forest[1, 1].height.__ge__(forest[2, 4].height),
    )

    a_tree = forest[4, 2]
    x = -2
    y = 1
    print(f"tree height {a_tree.height} at {a_tree.x_i}, {a_tree.y_i} coordinates")
    print(
        f"Compare trees using relative {x}, {y} coordinates:",
        forest[a_tree.x_i + x, a_tree.y_i + y].height,
    )
    print("Out of forest coordinate error:", forest[5, 6])


if __name__ == "__main__":
    main()
