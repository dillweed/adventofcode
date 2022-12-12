import re

# Read the input file and store its lines in a list
with open("03_input.txt") as file:
    input_list = file.readlines()


def replace_letters_with_numbers(text):
    # Define the pattern to match letters
    pattern = r"[a-zA-Z]"

    # Replace the matched letters with their corresponding numbers
    return re.sub(
        pattern,
        lambda m: str(
            ord(m.group(0).lower()) - ord("a") + 1 + (26 if m.group(0).isupper() else 0)
        ),
        text,
    )


# Initialize the priority sum
priority_sum = 0

for group in zip(input_list[::3], input_list[1::3], input_list[2::3]):
    found = False
    group = list(group)
    for i, item in enumerate(group):
        group[i] = item.strip()
    print(group)
    for _c in group[0]:
        if found:
            break
        else:
            if _c in group[1] and _c in group[2]:
                print(_c)
                found = True
                priority_sum += int(replace_letters_with_numbers(_c))

# Print the final priority sum
print(priority_sum)
