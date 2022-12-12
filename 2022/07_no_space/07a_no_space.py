"""TBA."""


def main():
    # Load input string as list
    input_list = load_input_file()
    # find sum of dirs of size less than 1000000
    sum = sum_small_dirs(input_list)
    print(sum)


def sum_small_dirs(input_list: list[str]) -> int:

    return 1


def load_input_file():
    with open("07_input_test.txt") as file:
        raw_input_list = file.readlines()

    input_list = []
    for line in raw_input_list:
        input_list.append(line.strip("\n"))

    return input_list


if __name__ == "__main__":
    main()
