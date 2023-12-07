from day_3.solution import part_1

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
