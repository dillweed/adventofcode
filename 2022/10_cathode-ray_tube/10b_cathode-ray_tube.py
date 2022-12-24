from pprint import pprint
from grapher import Grapher

"""Process signal input to find answer to 10b."""


def main():
    """TBA."""
    height = 6
    width = 40
    graph = Grapher(height, width)
    print(graph.display())
    # Define input filename
    input_file = "10_input_test.txt"
    # Load input string as list
    signal = load_input_file(input_file)
    cycles = process_signal(signal)
    i_cycles = list((i, cycle) for i, cycle in enumerate(cycles))
    for i in range(len(i_cycles) - 1):
        print(i, i_cycles[i])
        # TODO verify separation of rows. Should be 0 through 39 each.
        # TODO also verify if statement for valid -m+ values
        # If rows are correct, the issue may be in process_signal.
        if i_cycles[i][0] - (width * (i_cycles[i][0] // width)) in range(
            i_cycles[i][1] - 1, i_cycles[i][1] + 2
        ):
            graph.set_value(
                i_cycles[i][0] - (width * (i_cycles[i][0] // width)),
                height - (i_cycles[i][0] // width + 1),
                "#",
            )
            print(graph.display())
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
