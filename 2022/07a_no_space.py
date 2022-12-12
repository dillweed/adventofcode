with open("07_input_test.txt") as file:
    raw_input_list = file.readlines()

input_list = []
for line in raw_input_list:
    input_list.append(line.strip("\n"))
