# Setup
result = 0
input_file = 'input.txt'

def find_calibration_value(line):
    digits = ''
    # Find first digit
    for char in line:
        if char.isdigit():
            digits += char
            break

    # Find last digit
    for char in line[::-1]:
        if char.isdigit():
            digits += char
            break
    
    return digits

with open(input_file, 'r', encoding='utf-8') as input:
    for line in input:
        calibration_value = find_calibration_value(line)
        result += int(calibration_value)

    print(result)
            