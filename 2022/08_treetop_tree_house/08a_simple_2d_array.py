def main():
    with open("08_input_test.txt") as file:
        trees_str = file.read()
    print(trees_str)
    lines = trees_str.strip().split("\n")
    heights = [[int(ch) for ch in line] for line in lines]
    forest_y_max = len(heights)
    forest_x_max = len(heights[0][:])

    # This would have been an easier way to reference
    # tree height by x, y coordinates.
    print(heights[3][2])


if __name__ == "__main__":
    main()
