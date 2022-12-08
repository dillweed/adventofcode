import re

with open("03_input.txt") as file:
    input_list = file.readlines()


def replace_letters_with_numbers(text):
    pattern = r"[a-zA-Z]"
    return re.sub(
        pattern,
        lambda m: str(
            ord(m.group(0).lower()) - ord("a") + 1 + (26 if m.group(0).isupper() else 0)
        ),
        text,
    )


unique_items = []
priority_sum = 0

for line in input_list:
    middle = len(line) // 2
    found = False
    for _c in line[:middle]:
        if found:
            break
        if _c in line[middle:]:
            found = True
            priority_sum += int(replace_letters_with_numbers(_c))

print(priority_sum)
