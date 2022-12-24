from pprint import pprint

"""Process signal input to find answer to 10a."""


def main():
    """TBA."""
    # Define input filename
    input_file = "10_input_test.txt"
    # Load input string as list
    signal = load_input_file(input_file)
    # [print(line) for line in signal]
    cycles, cycles_with_addx = process_signal(signal)
    # pprint(cycles)
    # print(cycles[220])
    # pprint(list((i, cycle) for i, cycle in enumerate(cycles)))
    pprint(list((i, cycle) for i, cycle in enumerate(cycles_with_addx)))
    start = 20
    interval = 40
    strengths = query_cycles(cycles, start, interval)
    pprint(strengths)
    print(sum(strengths))


def process_signal(signal):
    cycles = [1]
    # TODO add another list for comparison to addx values
    cycles_with_addx = [0]
    target_cycle = 0
    pending = 0
    for item in signal:
        current_cycle = len(cycles)
        if current_cycle == target_cycle:
            cycles.append(cycles[-1] + pending)
            cycles_with_addx.append(
                ("n:", (cycles[-1]), "added", pending, "next", item)
            )
        else:
            cycles.append(cycles[-1])
            cycles_with_addx.append(("n:", (cycles[-1]), "prev noop", item))

        if item != None:  # Found an int
            cycles.append(cycles[-1])
            cycles_with_addx.append(("n:", (cycles[-1]), "pending", item))
            target_cycle = len(cycles)
            pending = item

    return cycles, cycles_with_addx


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
