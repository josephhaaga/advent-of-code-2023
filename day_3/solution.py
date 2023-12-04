import re
from typing import Dict
from typing import List
from typing import Tuple


def part_1(lines: List[str]):
    # lines = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    # ]
    ...


def main() -> int:
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")[:-1]

    print(part_1(lines))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
