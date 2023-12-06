from dataclasses import dataclass
import re
from typing import Dict
from typing import List
from typing import Tuple
from typing import Optional


@dataclass
class Number:
    value: int
    counted: bool = False


class Board:
    def __init__(self, lines: List[str]):
        self.height: int = len(lines)
        self.width: int = len(lines[0])
        self.numbers, self.symbols = self._parse_lines(lines)


    def get_number_at(self, x: int, y: int) -> Optional[Number]:
        try:
            return self.numbers[x][y]
        except IndexError:
            return None


    def get_adjacent_indexes(self, row: int, col: int) -> List[Tuple[int, int]]:
        """Return the indexes of adjacent cells."""
        ret = []
        for y in range(max(0, row-1), min(self.height, row+1) + 1):
            for x in range(max(0, col-1), min(self.width, col+1) + 1):
                ret += [(y, x)]
        return ret


    def _parse_lines(self, lines: List[str]) -> (List[List[Optional[Number]]], List[Tuple[int, int]]):
        symbols: List[Tuple[int, int]] = []
        nums: List[List[Optional[Number]]] = []
        for row, line in enumerate(lines):
            new_row = []
            l, r = 0, 0
            while l < len(line):
                if not line[l].isnumeric():
                    if line[l] != ".":
                        symbols += [(row, l)]
                    new_row += [None]
                    l += 1
                    r = l
                elif not line[r].isnumeric():
                    number = Number(value=int(line[l:r]))
                    new_row += [number] * (r - l)
                    l = r
                r += 1
            nums += [new_row]
        return nums, symbols


def part_1(lines: List[str]) -> int:
    board = Board(lines)
    neighbor_numbers = []
    print(f"{board.symbols=}")
    for (r, c) in board.symbols: # (1, 3)
        print(f" {(r, c)=}")
        print(f" {board.get_adjacent_indexes(r, c)=}")
        for (i, j) in board.get_adjacent_indexes(r, c):
            val = board.get_number_at(i, j)
            if val:
                neighbor_numbers += [val]
    ans = 0
    for num in neighbor_numbers:
        ans += num.value if not num.counted else 0
        num.counted = True
    return ans


def main() -> int:
    with open("day_3/input.txt", "r") as f:
        lines = f.read().split("\n")[:-1]

    print(part_1(lines))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
