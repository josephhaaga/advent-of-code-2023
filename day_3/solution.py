import re
from typing import Iterator
from typing import List
from typing import Tuple


def border_indexes(row, start, end, width, height) -> List[Tuple[int, int]]:
    res = []

    min_row, max_row = max(0, row - 1), min(row + 1, height - 1)
    min_col, max_col = max(0, start - 1), min(end, width - 1)
    prohibited = [(row, c) for c in range(start, end)]

    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if (r, c) not in prohibited:
                res += [(r, c)]

    return res


def is_part_number(lines: list[str], row: int, col: tuple[int, int]) -> bool:
    """determine if the number at lines[row][col[0]:col[1]] is a part number."""
    w, h = len(lines[0]), len(lines)
    s, e = col
    for r, c in border_indexes(row=row, start=s, end=e, width=w, height=h):
        char = lines[r][c]
        char_is_a_symbol = char != "." and not char.isnumeric()
        if char_is_a_symbol:
            return True
    return False


def part_1(lines: List[str]) -> int:
    s = 0
    pat = re.compile(r"(\d+)")
    for row, line in enumerate(lines):
        row_total = 0
        matches: Iterator[re.Match] = pat.finditer(line)
        for match in matches:
            cols = match.span()
            number = line[cols[0] : cols[1]]
            part_number = is_part_number(lines, row, cols)
            if part_number:
                row_total += int(number)
        s += row_total
    return s


def part_2(lines: List[str]) -> int:
    return 0


def main() -> int:
    with open("day_3/input.txt", "r") as f:
        lines = f.read().split("\n")[:-1]

    print(part_1(lines))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
