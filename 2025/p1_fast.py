#!/usr/bin/env python3
import sys

def solve(path: str) -> int:
    dial = 50
    zeros = 0
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            dir_, num = line[0], int(line[1:])
            step = -num if dir_ == "L" else num
            dial = (dial + step) % 100
            if dial == 0:
                zeros += 1
    return zeros


def main(argv: list[str]) -> None:
    path = argv[1] if len(argv) > 1 else "input.txt"
    print(solve(path))


if __name__ == "__main__":
    main(sys.argv)
