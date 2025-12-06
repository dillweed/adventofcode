NUMBER_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        return file_content

def find_first_digit(line):
    i = 0
    digit = ''
    while i < len(line):
        if line[i].isdigit():
            digit = line[i]
            # print('line:', line, 'i:', i, 'char:', digit)
        else:
            for word in NUMBER_MAP:
                if i + len(word) <= len(line) and line[i:i+len(word)].lower() == word:
                    digit = NUMBER_MAP[word]
                    # print('line:', line, 'i:', i, 'word:', digit)
        if digit:
            return digit
        else: 
            i += 1

def find_last_digit(line):
    i = 0
    line = line[::-1]
    digit = ''
    while i < len(line):
        if line[i].isdigit():
            digit = line[i]
            # print('line:', line, 'i:', i, 'char:', digit)
        else:
            for word in NUMBER_MAP:
                if i + len(word) <= len(line) and line[i:i+len(word)].lower() == word[::-1]:
                    digit = NUMBER_MAP[word]
                    # print('line:', line, 'i:', i, 'word:', digit)
        if digit:
            return digit
        else: 
            i += 1

def get_line_calibration(line):
    first_digit = find_first_digit(line)
    last_digit = find_last_digit(line)
    return f'{first_digit}{last_digit}'

def calculate_result(file_content):
    calibration_sum = 0
    lines = file_content.splitlines()
    for line in lines:
        line_calibration = get_line_calibration(line)
        calibration_sum += int(line_calibration)
    return calibration_sum

if __name__ == "__main__":
    # Get input from file path
    input_data = load_file('input.txt')

    # Calculate result from input
    calibration_sum = calculate_result(input_data)

    # Display result
    print(f'Result: {calibration_sum}')