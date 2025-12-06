from pprint import pprint
from grapher import Grapher

"""Process signal input to find answer to 10b."""


def main():
    """TBA."""
    width = 40
    height = 6
    fill = "🎄"
    lettering = "🎁"
    graph = Grapher(width, height, fill=fill)
    # Define input filename
    input_file = "10_input.txt"
    # Load input string as list
    signal = load_input_file(input_file)
    cycles = process_signal(signal)
    # Had to drop the first cycle to get the right output
    i_cycles = list((i, cycle) for i, cycle in enumerate(cycles[1:]))
    for i in range(len(i_cycles)):  # drop the last cycle
        # This print verifies line segment indexes and sprite window values
        # compared to cycle index
        # print(
        #     f"i: {i_cycles[i][0] - (width * (i_cycles[i][0] // width))} in range({i_cycles[i][1] - 1} to {i_cycles[i][1] + 2}) for v: {i_cycles[i][1]}"
        # )

        if i_cycles[i][0] - (width * (i_cycles[i][0] // width)) in range(
            i_cycles[i][1] - 1, i_cycles[i][1] + 2
        ):
            graph.set_value(
                i_cycles[i][0] - (width * (i_cycles[i][0] // width)),
                height - (i_cycles[i][0] // width + 1),
                lettering,
            )
    print(graph.display())


def process_signal(signal):
    cycles = [1]
    target_cycle = 0
    pending = 0
    for item in signal:
        current_cycle = len(cycles)
        if current_cycle == target_cycle:
            cycles.append(cycles[-1] + pending)
        else:
            cycles.append(cycles[-1])
        if item != None:  # Found an int
            cycles.append(cycles[-1])
            target_cycle = len(cycles)
            pending = item

    return cycles


def query_cycles(cycles, start, interval):
    strengths = []
    for i in range(start, len(cycles), interval):
        strengths.append(cycles[i] * i)
    return strengths


def load_input_file(input_file) -> list:
    signal = []
    with open(input_file) as file:
        for line in file.readlines():
            if line.strip() != "noop":
                # Throw away "addx" and keep int
                signal.append(int(line.split()[1]))
            else:
                # add a blank
                signal.append(None)

    return signal


if __name__ == "__main__":
    main()
