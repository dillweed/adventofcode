# Read the input datastream file and store as a string
with open("06_input.txt") as file:
    signal = file.read()

set_min = 14
# Init flag to break loop if found
found = False
# loop through the characters in the signal string
for i, c in enumerate(signal):
    if found:
        break
    # check if length of set of substring is set_min
    if len(set(signal[i : i + set_min])) == set_min:
        print(set(signal[i : i + set_min]))
        print(i + set_min)
        found = True
