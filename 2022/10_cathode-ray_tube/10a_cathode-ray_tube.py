"""TBA."""


def main():
    """TBA."""
    # Define input filename
    input_file = "10_input_test.txt"
    # Load input string as list
    signal = load_input_file(input_file)
    [print(line) for line in signal]


def load_input_file(input_file) -> list:
    signal = []
    with open(input_file) as file:
        for line in file.readlines():
            if line.strip() != 'noop':
                # Throw away "addx" and keep int
                signal.append(int(line.split()[1]))
            else:
                # Keep "noop"
                signal.append(line.strip())

    return signal


if __name__ == "__main__":
    main()
