from pprint import pprint

"""Process signal input to find answer to 10a."""


def main():
    """TBA."""
    # Define input filename
    input_file = "10_input_test.txt"
    # Load input string as list
    signal = load_input_file(input_file)
    cycles = process_signal(signal)
    # print(cycles)
    print(cycles[220])

    start = 20
    interval = 40
    strengths = query_cycles(cycles, start, interval)
    pprint(strengths)
    print(sum(strengths))


def process_signal(signal):
    total = 1
    cycles = [1, 1]  # Not sure why I have to pad this list
    for item in signal:
        cycles.append((total))
        if item != None:
            total += int(item)
            cycles.append((total))
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
