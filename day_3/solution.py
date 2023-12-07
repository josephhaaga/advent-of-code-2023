from typing import List
from typing import Tuple



def part_1(lines: List[str]) -> int:
    height = len(lines)
    width = len(lines[0])

    row = 0
    while row < height:
        
        row += 1

    return 1


def main() -> int:
    with open("day_3/input.txt", "r") as f:
        lines = f.read().split("\n")[:-1]

    print(part_1(lines))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
