test = [3, 2, 2, 4, 5, 3]

# Find the value at index 0
first_value = test[0]

# Initialize a variable to store the index offset
offset = -1

# Loop through the list, starting from the second element
for i in range(1, len(test)):
    # If the current value is equal to or greater than the first value,
    # store the index offset and break out of the loop
    if test[i] >= first_value:
        offset = i
        break

# Print the index offset
print(offset)
