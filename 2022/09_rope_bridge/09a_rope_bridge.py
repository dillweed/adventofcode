from pprint import pprint

"""TBA."""
# Per instructions:
# If the head is ever two steps directly up, down, left, or right from the tail,
# the tail must also move one step in that direction so it remains close enough.
# Otherwise, if the head and tail aren't touching and aren't in the same row or
# column, the tail always moves one step diagonally to keep up.


def main():
    """TBA."""
    # Define input filename
    input_file = "09_input.txt"
    # Load input string as list
    motions = load_input_file(input_file)
    # Display motion list
    pprint(motions, width=10)
    # Process motion list
    visited = move(motions)
    pprint(visited, width=10)
    # How many unique xy coordinates did tail visit?
    print(len(set(visited)))


def move(motions: list[tuple]) -> list:
    visited: list[tuple[int, int]] = []  # Coords visited by tail
    head = (0, 0)  # Head x, y coordinate start
    tail = (0, 0)  # Tail x, y coordinate start
    visited.append(head)  # Record first position
    for motion in motions:
        for _ in range(motion[1]):
            head = lead(motion[0], head)
            tail = follow(head, tail)
            visited.append(tail)
    return visited


def lead(direction, head: tuple[int, int]) -> tuple[int, int]:
    if direction == "R":  # Right
        head = head[0] + 1, head[1]
    if direction == "L":  # Left
        head = head[0] - 1, head[1]
    if direction == "U":  # Up
        head = head[0], head[1] + 1
    if direction == "D":  # Down
        head = head[0], head[1] - 1
    return head


def follow(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]
    # tail should always fall in xy line with head and never drag along diagonally.
    # Assign the smaller head axis to tail and half of the larger tail diff.
    if abs(diff_x) > 1:  # tail is 2 away on x axis
        return (tail[0] + diff_x // 2, head[1])
    if abs(diff_y) > 1:  # tail is 2 away on y axis
        return (head[0], tail[1] + diff_y // 2)
    return tail  # head and tail are adjacent. No movement required.


def load_input_file(input_file) -> list:
    with open(input_file) as file:
        motions = [
            (m, int(n)) for line in file.readlines() for m, n in [line.strip().split()]
        ]

    return motions


if __name__ == "__main__":
    main()
