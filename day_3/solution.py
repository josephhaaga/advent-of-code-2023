import re
from typing import List
from typing import Tuple


def border_indexes(row, start, end, width, height) -> List[Tuple[int, int]]:
    res = []

    min_row, max_row = max(0, row-1), min(row+1, height-1)
    min_col, max_col = max(0, start-1), min(end+1, width-1)
    prohibited = [(row, c) for c in range(start, end+1)]

    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if (r, c) not in prohibited:
                res += [(r, c)]

    return res


def is_part_number(lines: List[str], row: int, col: Tuple[int, int]) -> bool:
    """Determine if the number at lines[row][col[0]:col[1]] is a Part Number."""
    l, r = col
    cols = range(
        max(0, l-1),
        min(r+2, len(lines[0]))
    )
    rows = range(
        max(0, row-1),
        min(row+2, len(lines))
    )
    for i in rows:
        for j in cols:
            currently_on_original_number = (i == row and l < j < r)
            if currently_on_original_number:
                continue
            char = lines[i][j]
            char_is_a_symbol = (char != "." and not char.isnumeric())
            if char_is_a_symbol:
                return True
    return False


def part_1(lines: List[str]) -> int:
    s = 0
    pat = re.compile(r'(\d+)')
    for row, line in enumerate(lines):
        row_total = 0
        matches: List[re.Match] = pat.finditer(line)
        for match in matches:
            cols = match.span()
            number = line[cols[0]:cols[1]]
            part_number = is_part_number(lines, row, cols)
            if part_number:
                row_total += int(number)
        s += row_total
    return s


def main() -> int:
    with open("day_3/input.txt", "r") as f:
        lines = f.read().split("\n")[:-1]

    print(part_1(lines))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
