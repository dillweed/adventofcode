from dataclasses import dataclass, asdict, astuple, field
from pprint import pprint
from collections import defaultdict


def main():
    """TBA."""

    input_file = "08_input_test.txt"
    forest = load_forest(input_file)
    max_x = max([tree._x for tree in forest.values()])
    max_y = max([tree._y for tree in forest.values()])

    print("Visible trees:", sum([tree.visible for tree in forest.values()]))

    # if forest[3, 2]:
    #     print(max_x, max_y)

    # # Change attributes after instantiation
    # forest[3, 2].view.append("aoeu")
    # forest[3, 2].view.append(234)
    # print("Updated tree:", forest[3, 2])

    # print(
    #     "Compare heights using absolute coordinates",
    #     forest[1, 1].height.__ge__(forest[2, 4].height),
    # )

    # a_tree = forest[4, 2]
    # x = -2
    # y = 1
    # print(f"tree height {a_tree.height} at {a_tree._x}, {a_tree._y} coordinates")
    # print(
    #     f"Compare trees using relative {x}, {y} coordinates:",
    #     forest[a_tree._x + x, a_tree._y + y].height,
    # )
    # print("Out of forest coordinate error:", forest[5, 6])


def load_forest(input_file) -> dict:
    trees_list = load_input_file(input_file)
    forest: dict = defaultdict(lambda: None)
    for y, line in enumerate(trees_list):
        for x, height in enumerate(line):
            this_tree = Tree(x, y, height, list_i=len(forest))
            forest[x, y] = this_tree
    return forest


@dataclass(frozen=True)
class Tree:
    _x: int
    _y: int
    height: int
    list_i: int
    edge: bool = False
    view: list[int] = field(default_factory=list)
    visible: bool = False

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


if __name__ == "__main__":
    main()
