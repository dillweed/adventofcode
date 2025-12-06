test = [3, 0, 3, 7, 3]


def view_distance_forward(house_i, line) -> int:
    distance = 0
    offset = -1
    for view_i in range(house_i + 1, len(line)):
        print(
            "subloop forward",
            "house n:",
            line[house_i],
            "view_i:",
            view_i,
            "view n:",
            line[view_i],
        )
        if line[view_i] >= line[house_i]:
            offset = view_i - house_i
            print("offset", offset)
            break
    if offset == -1:  # no trees >= found
        distance = len(line) - 1 - house_i
    else:
        distance = offset
    return distance


def view_distance_behind(house_i, line) -> int:
    distance = 0
    offset = -1
    for view_i in range(house_i - 1, -1, -1):
        print(
            "subloop behind",
            "house n:",
            line[house_i],
            "view_i:",
            view_i,
            "view n:",
            line[view_i],
        )
        if line[view_i] >= line[house_i]:
            offset = house_i - view_i
            print("offset", offset)
            break
    if offset == -1:  # no trees >= found
        distance = house_i
    else:
        distance = offset
    return distance


result = []
result.append(view_distance_behind(0, test))

# for i in range(len(test)):
#     print("main", i)
#     result.append(view_distance(i, test))
print(result)
