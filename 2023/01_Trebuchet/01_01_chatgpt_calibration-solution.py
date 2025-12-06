# Improved version of the calibration value extraction code

def find_first_digit(line):
    """Finds and returns the first digit in the given line."""
    for char in line:
        if char.isdigit():
            return char
    return None  # Explicitly return None if no digit is found

def find_last_digit(line):
    """Finds and returns the last digit in the given line."""
    for char in reversed(line):
        if char.isdigit():
            return char
    return None  # Explicitly return None if no digit is found

def find_calibration_value(line):
    """Combines the first and last digits to form a two-digit number."""
    first_digit = find_first_digit(line)
    last_digit = find_last_digit(line)
    
    if first_digit and last_digit:
        return f"{first_digit}{last_digit}"
    else:
        raise ValueError("Line does not contain sufficient digits")

def calculate_total_calibration(input_file):
    total_calibration_sum = 0

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                calibration_value = find_calibration_value(line.strip())
                total_calibration_sum += int(calibration_value)
            except ValueError as e:
                print(f"Skipping line: {e}")
    
    return total_calibration_sum

# Execute and print result
if __name__ == "__main__":
    input_file = 'input.txt'
    result = calculate_total_calibration(input_file)
    print(f"Total Calibration Sum: {result}")