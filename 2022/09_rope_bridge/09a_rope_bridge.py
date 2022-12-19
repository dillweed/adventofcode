from pprint import pprint

"""TBA."""


def main():
    """TBA."""
    # Define input filename
    input_file = "09_input_test.txt"
    # Load input string as list
    motions = load_input_file(input_file)
    pprint(motions, width=10)

    # Track coordinates T visits in a list. Could be a set to avoid dupes. Start (0,0)
    # Loop motions for H.
    # After H move, check T and H relative positions.
    # If not adjacent, update T position.
    # Touching is adjacent horizontally, vertically, diagonally adjacent or overlapping.
    # T should follow a non-adjacent H ....
    # Do H or T ever leap or only move one step at a time? No.
    # Do I need different functions for NSEW movement vs diagonal?

    # If the head is ever two steps directly up, down, left, or right from the tail,
    # the tail must also move one step in that direction so it remains close enough.
    # Otherwise, if the head and tail aren't touching and aren't in the same row or
    # column, the tail always moves one step diagonally to keep up.


def load_input_file(input_file) -> list:
    with open(input_file) as file:
        motions = [
            (m, int(n)) for line in file.readlines() for m, n in [line.strip().split()]
        ]

    return motions


if __name__ == "__main__":
    main()
