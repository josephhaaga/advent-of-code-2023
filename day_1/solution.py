import re
from typing import Tuple


def get_calibration_value(line: str) -> int:
    """Extract first and last digits in `line` to form a two-digit number"""
    left, right = None, None
    for i in range(0, len(line)):
        if line[i].isnumeric():
            left = line[i]
            break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            right = line[i]
            break
    return int(f"{left}{right}")


WORD_TO_DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_words_with_digits(line: str) -> str:
    """Replace all spelled-out numbers in `line` with digits."""
    words = list(WORD_TO_DIGIT.keys())
    i = 0
    while i < len(line) - 2:
        for j in range(i + 3, i + 6):
            subword = line[i:j]
            if subword in words:
                match = WORD_TO_DIGIT[subword]
                line = line[:i] + match + line[j:]
        i += 1
    return line


def main() -> int:
    with open("day_1/input.txt", "r") as f:
        lines = f.read().split("\n")[:-1]

    part_1 = 0
    for line in lines:
        part_1 += get_calibration_value(line)
    print(f"{part_1=}")

    part_2 = 0
    for line in lines:
        l = replace_words_with_digits(line)
        part_2 += get_calibration_value(l)
    print(f"{part_2=}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
