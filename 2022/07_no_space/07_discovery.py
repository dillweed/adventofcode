from collections import Counter

# QUESTIONS:
#
# Does the dir transversal repeat dirs?
# No, some names repeat, but dirs are only listed once
#
# What is the transversal algorithm?
# ls, if sub dirs, cd into next sub
# else cd .., if more siblings, cd next sibling
# else cd ..
#
# What algorithm should I use for 07a?
# Looking like recursion for any ls that finds dirs.

# Read input to list
with open("07_input.txt") as file:
    raw_input_list = file.readlines()

# Clean \n chars
input_list = []
for line in raw_input_list:
    input_list.append(line.strip("\n"))

# For main input, some dir names are repeated.
# len(dirs_list) was 188
# len(set(dirs_list)) was 139
dirs_list = []
for line in input_list:
    if line.startswith("dir "):
        dirs_list.append(line.replace("dir ", ""))

dir_counts = dict(Counter(dirs_list))
dir_duplicates = {key: value for key, value in dir_counts.items() if value > 1}
print("dir name dups:", dir_duplicates)
print("dirs list len:", len(dirs_list))
print("dirs set len:", len(set(dirs_list)))

# For main input, some file names are repeated.
# len(file_list) was 271
# len(set(file_list)) was 169
# Confirmed file lines are consistently [size]" "[name]
file_list = []
for line in input_list:
    if line[0].isdigit():
        file_list.append(line.split()[1])

file_counts = dict(Counter(file_list))
file_duplicates = {key: value for key, value in file_counts.items() if value > 1}
print("file name dups:", file_duplicates)
print("files list len:", len(file_list))
print("files set len:", len(set(file_list)))

# Write list with indentation to see dir depth
# input_indented = ""
# indent = 0
# for line in input_list:
#     if line[:4] == "$ cd" and ".." not in line:
#         indent += 1
#         input_indented += (line) + "\n"
#     if line[:4] == "$ cd" and ".." in line:
#         indent -= 1
#         input_indented += (line) + "\n"
#     if line[:4] == "$ ls":
#         input_indented += (line) + "\n"
#     if line[0] == "d":
#         input_indented += ("    " * indent) + line + "\n"
#     if line[0].isdigit():
#         input_indented += ("    " * indent) + line + "\n"

# with open("07_input_indented.txt", "w") as file:
#     file.write(input_indented)
