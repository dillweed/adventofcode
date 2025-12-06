NUMBER_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
        return file_content


def find_digit(line, search_from_end=False):
    if search_from_end:
        line = line[::-1]

    for i, char in enumerate(line):
        if char.isdigit():
            return char
        for word, num in NUMBER_MAP.items():
            if i + len(word) <= len(line) and line[i : i + len(word)].lower() == (
                word if not search_from_end else word[::-1]
            ):
                return num
    return ""


def get_line_calibration(line):
    first_digit = find_digit(line)
    last_digit = find_digit(line, search_from_end=True)
    return f"{first_digit}{last_digit}"


def calculate_result(file_content):
    return sum(int(get_line_calibration(line)) for line in file_content.splitlines())


if __name__ == "__main__":
    input_data = load_file("input.txt")
    calibration_sum = calculate_result(input_data)
    print(f"Result: {calibration_sum}")
