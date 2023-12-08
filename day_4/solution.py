import math
import re
from typing import Iterator
from typing import List
from typing import Tuple


def fib(n: int) -> int:
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * fib(n-1)


def part_1(lines: List[str]) -> int:
    result = 0
    number_pattern = re.compile(r"(\d+)")
    for card in lines:
        card_numbers = card.split(":")[1]
        winning_numbers, my_numbers = [
            [int(m.group(0)) for m in number_pattern.finditer(section)]
            for section in card_numbers.split("|")
        ]
        matches = len(set(winning_numbers).intersection(set(my_numbers)))
        result += fib(matches)

    return result


def part_2(lines: List[str]) -> int:
    return 0


def main() -> int:
    with open("day_4/input.txt", "r") as f:
        lines = f.read().split("\n")[:-1]

    print(f"{part_1(lines)=}")
    print(f"{part_2(lines)=}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
