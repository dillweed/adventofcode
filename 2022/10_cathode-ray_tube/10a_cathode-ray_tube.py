from pprint import pprint
"""TBA."""


def main():
    """TBA."""
    # Define input filename
    input_file = "10_input.txt"
    # Load input string as list
    signal = load_input_file(input_file)
    # [print(line) for line in signal]
    cycles = process_signal(signal)
    pprint(cycles)
    print(cycles[220])
    pprint(list((i, cycle) for i, cycle in enumerate(cycles)))
    start = 20
    interval = 40
    strengths = query_cycles(cycles, start, interval)
    pprint(strengths)
    print(sum(strengths))


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


# def process_signal(signal):
#     cycles = [1]
#     last_item = 0
#     for item in signal:
#         last_item = item
#         if item == None:
#             if last_item != None:
#                 cycles.append(cycles[-1] + last_item)
#                 break
#             cycles.append(cycles[-1])
#         else:
#             if last_item != None:
#                 cycles.append(cycles[-1] + last_item)
#                 cycles.append(cycles[-1])
#                 break
#             cycles.append(cycles[-1])
#             cycles.append(cycles[-1])
#     return cycles


def query_cycles(cycles, start, interval):
    strengths = []
    for i in range(start, len(cycles), interval):
        strengths.append(cycles[i]*i)
    return strengths


def load_input_file(input_file) -> list:
    signal = []
    with open(input_file) as file:
        for line in file.readlines():
            if line.strip() != 'noop':
                # Throw away "addx" and keep int
                signal.append(int(line.split()[1]))
            else:
                # add a blank
                signal.append(None)

    return signal


if __name__ == "__main__":
    main()
