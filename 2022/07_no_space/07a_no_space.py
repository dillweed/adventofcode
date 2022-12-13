"""TBA."""


def main():
    """TBA."""
    # Define input filename
    input_file = "07_input.txt"
    # input_file = "07_input.txt"
    # Load input string as list
    input_list = load_input_file(input_file)
    # Set threshold for dir size
    limit = 100000
    # Start running sum
    sum = 0
    # Init list_index for to track line
    list_index = 0
    # find sum of dirs
    total_sum, list_index, sum = sum_dirs(input_list, list_index, limit, sum)
    print(
        f"total_sum: {total_sum}, end list_index: {list_index + 1}, dir sum under limit: {sum}"
    )


def sum_dirs(
    input_list: list[str], list_index: int, limit: int, sum: int
) -> tuple[int, int, int]:
    """TBA."""
    local_sum = 0  # file size sum for current dir
    lower_dir_sums = 0
    end_ls = False  # flag True if ls finished
    while list_index < len(input_list) - 1:
        list_index += 1
        line = input_list[list_index]
        if end_ls:  # ls output is finished
            print("ls is finished. break.")
            break
        print(f"list item {list_index + 1}:", line)
        if line.startswith("$ cd"):
            end_ls = True
            if line == "$ cd ..":
                # .. indicates bottom of dir and end of recursion
                print("met ..")
                if local_sum <= limit:
                    print(f"adding local sum {local_sum} to sum {sum}")
                    sum += local_sum
                    print(f"new sum: {sum}")
                else:
                    print(f"local_sum {local_sum} over {limit}")
                return local_sum, list_index, sum
            print("begin next recursive iteration")
            lower_dir_sums, list_index, sum = sum_dirs(
                input_list, list_index, limit, sum
            )
            print(f"adding lower_dir_sums {lower_dir_sums} to local_sum {local_sum}")
            local_sum += lower_dir_sums
            print(f"new local_sum: {local_sum}")
            end_ls = False
        if line[0].isdigit():  # file size detected
            local_sum += int(line.split()[0])
            print("local_sum:", local_sum)

    print("REACHED END OF LOOP. Unwinding. local_sum", local_sum)
    if local_sum <= limit:
        sum += local_sum

    return local_sum, list_index, sum


def load_input_file(input_file) -> list[str]:
    with open(input_file) as file:
        raw_input_list = file.readlines()

    input_list = []
    for line in raw_input_list:
        input_list.append(line.strip("\n"))

    return input_list


if __name__ == "__main__":
    main()
