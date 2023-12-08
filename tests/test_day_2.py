import pytest

from day_2.solution import game_is_possible
from day_2.solution import parse_constraint
from day_2.solution import parse_game_record
from day_2.solution import power_of_min_cubes


PART_1_INPUT = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

PART_1_CONSTRAINT = "12 red cubes, 13 green cubes, 14 blue cubes"

PART_1_POSSIBLE_GAMES = [True, True, False, False, True]


def test_parse_game_record():
    rec = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    out = parse_game_record(rec)
    assert out == [
        {"red": 6, "blue": 1, "green": 3},
        {"red": 1, "blue": 2, "green": 2},
    ]


@pytest.mark.parametrize(
    "record, constraint, output",
    zip(
        PART_1_INPUT.split("\n")[1:],
        [PART_1_CONSTRAINT] * len(PART_1_POSSIBLE_GAMES),
        PART_1_POSSIBLE_GAMES,
    ),
)
def test_game_is_possible(record, constraint, output):
    assert game_is_possible(record, constraint) == output


PART_2_POWER_OF_SET_OF_CUBES = [48, 12, 1560, 630, 36]


@pytest.mark.parametrize(
    "record, constraint, output",
    zip(
        PART_1_INPUT.split("\n")[1:],
        [PART_1_CONSTRAINT] * len(PART_1_POSSIBLE_GAMES),
        PART_2_POWER_OF_SET_OF_CUBES,
    ),
)
def test_power_of_cubes(record, constraint, output):
    assert power_of_min_cubes(record, constraint) == output
