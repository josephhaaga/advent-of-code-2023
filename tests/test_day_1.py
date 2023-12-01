import pytest

from day_1.solution import get_calibration_value
from day_1.solution import replace_words_with_digits


PART_1_INPUT = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

PART_1_ANSWERS = [12, 38, 15, 77]


@pytest.mark.parametrize(
    'line, cal_val',
    zip(PART_1_INPUT.split("\n")[1:], PART_1_ANSWERS)
)
def test_get_calibration_value(line, cal_val):
    assert get_calibration_value(line) == cal_val


PART_2_INPUT = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

PART_2_ANSWERS = [29, 83, 13, 24, 42, 14, 76]


@pytest.mark.parametrize(
    "i, o",
    zip(
        PART_2_INPUT.split("\n")[1:],
        [
            "219",
            "8wo3",
            "abc123xyz",
            "x2ne34",
            "49872",
            "z1ight234",
            "7pqrst6teen"
        ]
    )
)
def test_replace_words_with_digits(i, o):
    assert replace_words_with_digits(i) == o


@pytest.mark.parametrize(
    "i, o",
    zip(PART_2_INPUT.split("\n")[1:], PART_2_ANSWERS)
)
def test_part_2(i, o):
    replaced = replace_words_with_digits(i)
    assert get_calibration_value(replaced) == o
