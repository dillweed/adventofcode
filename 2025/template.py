#!/usr/bin/env python3
import sys

def solve(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Start

def main(argv: list[str]) -> None:
    path = argv[1] if len(argv) > 1 else "input.txt"
    print(solve(path))

if __name__ == "__main__":
    main(sys.argv)
