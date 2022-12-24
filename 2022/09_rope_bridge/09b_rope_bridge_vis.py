from pprint import pprint
from collections import defaultdict
import time
import logger
from grapher import Grapher

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
    pprint(motions)
    # Init rope dict with start coordinate. Head will lead, and rope keys 1-9
    # will follow.
    rope = defaultdict(lambda: (0, 0))
    [rope[i] for i in range(1, 10)]
    # Process motion list
    visited_T, visited_H = move(motions, rope)
    # How many unique xy coordinates did tail visit?
    # print("All head positions")
    # pprint(visited_H)
    # print("All tail positions")
    # pprint(visited_T)
    # get_grapher_values(visited_H)
    print("Unique tail positions", len(set(visited_T)))


def get_grapher_values(visited):
    # Get values for Grapher
    x_visited = []
    y_visited = []
    for xy in visited:
        x_visited.append(xy[0])
        y_visited.append(xy[1])
    min_x = min(x_visited)
    max_x = max(x_visited)
    min_y = min(y_visited)
    max_y = max(y_visited)
    height = max_y - min_y + 1  # Add 1 for zero indexing
    width = max_x - min_x + 1  # Add 1 for zero indexing
    init_x = abs(min_x)  # X start position from left edge
    init_y = abs(min_y)  # Y start position from bottom edge
    print(f"min x: {min_x} max x: {max_x}")
    print(f"min y: {min_y} max y: {max_y}")
    print(f"height={height}, width={width}, init_x={init_x}, init_y={init_y}")


def move(motions: list[tuple], rope) -> list:
    visited_T = []  # Coords visited by tail
    visited_H = []  # Coords visited by head
    head = (0, 0)  # Head x, y coordinate start
    tail = (0, 0)  # Tail x, y coordinate start
    visited_H.append(head)  # Record first position
    visited_T.append(tail)  # Record first position
    graph = Grapher(305, 348, 119, 280)  # Dimensions 09b
    # graph = Grapher(26, 21, 11, 5)  # Dimensions of 09b test
    # graph = Grapher(6, 5, 0, 0)  # Dimensions of 09a test
    graph.set_value(0, 0, "S")  # Start 0,0
    with open("graph.txt", "w") as graph_file:
        graph_file.write(graph.display())
    for motion in motions:
        for _ in range(motion[1]):
            head = lead(motion[0], head)
            graph.set_value(0, 0, "S")
            graph.set_value(*visited_H[-1], ".")
            visited_H.append(head)
            graph.set_value(*head, "H")
            leader = head
            logger.log.info("motion: %s \niter: %s head: %s", motion, _, head)
            # Iterate through rope to let each knot follow the leader
            for key in rope.keys():
                graph.set_value(*rope[key], ".")
                rope[key] = follow(leader, rope[key])
                graph.set_value(*rope[key], key)
                leader = rope[key]
                # logger.log.info("key: %s, value: %s", key, rope[key])
            # Record all coords of tail
            visited_T.append(rope[len(rope.keys())])
            # time.sleep(.3)
            # with open("graph.txt", "w") as graph_file:
            #     graph_file.write(graph.display())
            # __ = input(
            # f"Motion: {motion} {_+1} of {motion[1]}. Enter to continue: ")
    [graph.set_value(*xy, "#") for xy in set(visited_T)]
    with open("graph.txt", "w") as graph_file:
        graph_file.write(graph.display())
    return visited_T, visited_H


def follow(leader: tuple[int, int], follower: tuple[int, int]) -> tuple[int, int]:
    diff_x = leader[0] - follower[0]
    diff_y = leader[1] - follower[1]
    if abs(diff_x) > 1 and diff_y == 0:  # follower is 2 away on x axis and on same y
        return (follower[0] + ((diff_x > 0) - (diff_x < 0)), follower[1])
    if abs(diff_y) > 1 and diff_x == 0:  # follower is 2 away on y axis and on same x
        return (follower[0], follower[1] + ((diff_y > 0) - (diff_y < 0)))
    # If x is 2 away and y is 1 away OR if x is 1 away and y is 2 away
    if (abs(diff_x) > 1 and abs(diff_y) >= 1) or (abs(diff_x) >= 1 and abs(diff_y) > 1):
        # Move diagonally towards the leader
        return (
            follower[0] + ((diff_x > 0) - (diff_x < 0)),
            follower[1] + ((diff_y > 0) - (diff_y < 0)),
        )
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
