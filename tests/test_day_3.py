from day_3.solution import part_1
from day_3.solution import border_indexes

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


def test_part_1():
    lines = PART_1_INPUT.split("\n")[1:]
    assert part_1(lines) == PART_1_ANSWER


def test_border_indexes():
    assert border_indexes(row=1, start=1, end=3, width=10, height=10) == [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
    ]
