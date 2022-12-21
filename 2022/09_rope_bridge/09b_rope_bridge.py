from pprint import pprint
from collections import defaultdict
import logger

"""TBA."""


def main():
    """TBA."""
    # Define input filename
    input_file = "09_input_testb.txt"
    # Load input string as list
    motions = load_input_file(input_file)
    # Display motion list
    pprint(motions)
    # Init rope dict with start coordinate. Head will lead, and rope keys 1-9
    # will follow.
    rope = defaultdict(lambda: (0, 0))
    [rope[i] for i in range(1, 10)]
    # Process motion list
    visited = move(motions, rope)
    # How many unique xy coordinates did tail visit?
    print(len(set(visited)))


def move(motions: list[tuple], rope) -> list:
    visited = []  # Coords visited by tail
    head = (0, 0)  # Head x, y coordinate start
    for motion in motions:
        for _ in range(motion[1]):
            head = lead(motion[0], head)
            leader = head
            logger.log.info("motion: %s \niter: %s head: %s", motion, _, head)
            # Iterate through rope to let each knot follow the leader
            for key in rope.keys():
                rope[key] = follow(leader, rope[key])
                leader = rope[key]
                logger.log.info("key: %s, value: %s", key, rope[key])
            visited.append(rope[len(rope.keys())])  # Record all coords of tail
    return visited


def follow(leader: tuple[int, int], follower: tuple[int, int]) -> tuple[int, int]:
    diff_x = leader[0] - follower[0]
    diff_y = leader[1] - follower[1]
    # follower should always fall in xy line with leader and never drag along diagonally.
    # Assign the smaller leader axis to follower and half of the larger follower diff.
    if abs(diff_x) > 1:  # follower is 2 away on x axis
        return (follower[0] + diff_x // 2, leader[1])
    if abs(diff_y) > 1:  # follower is 2 away on y axis
        return (leader[0], follower[1] + diff_y // 2)
    return follower  # leader and follower are adjacent. No movement required.


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


def load_input_file(input_file) -> list:
    with open(input_file) as file:
        motions = [
            (m, int(n)) for line in file.readlines() for m, n in [line.strip().split()]
        ]
    return motions


if __name__ == "__main__":
    main()
