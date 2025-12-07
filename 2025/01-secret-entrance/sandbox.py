#!/usr/bin/env python3
numbers = []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        numbers.append(int(line[1:]))

    print(sorted(numbers, reverse=True))