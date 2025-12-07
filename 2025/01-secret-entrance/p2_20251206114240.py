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
            if step < 0:
                for _ in range(abs(step)):
                    dial -= 1
                    dial = dial%100
                    zeros += (dial == 0)
            else:
                for _ in range(step):
                    dial += 1
                    dial = dial%100
                    zeros += (dial == 0)
        return zeros


def main(argv: list[str]) -> None:
    path = argv[1] if len(argv) > 1 else "input.txt"
    print(solve(path))


if __name__ == "__main__":
    main(sys.argv)
