from day_3.solution import part_1
from day_3.solution import Board, Number

import pytest


PART_1_INPUT = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

PART_1_ANSWER = 4361


@pytest.mark.skip
def test_board_parse_numbers():
    inp = ["467..114.."]
    b = Board(inp)
    out = b.numbers
    assert out == [[467, 467, 467, None, None, 114, 114, 114, None, None]]


def test_part_1():
    lines = PART_1_INPUT.split("\n")[1:]
    assert part_1(lines) == PART_1_ANSWER
