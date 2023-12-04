import re
from typing import Dict
from typing import List
from typing import Tuple



def parse_game_record(record: str) -> List[Tuple[int, str]]:
    """Extract observations from a single game record."""
    observations_pattern = re.compile(r' ((\d+) ([a-z]+))[,;]?')
    observations: List[Tuple[int, str]] = []
    for m in observations_pattern.findall(record):
        observations += [(int(m[1]), m[2])]
    return observations


def parse_constraint(constraint: str) -> List[Tuple[int, str]]:
    constraint_pattern = re.compile(r'((\d+) ([a-z]+) cubes)')
    constraints: List[Tuple[int, str]] = [
        (int(m[1]), m[2]) for m in constraint_pattern.findall(constraint)
    ]
    return constraints


def summarize_color_observations(record: List[Tuple[int, str]]) -> Dict[str, int]:
    """Return a map of `{color: count}`."""
    result = {}
    for (count, color) in record:
        if color not in result:
            result[color] = 0
        result[color] += count
    return result


def game_is_possible(record: str, constraint: str) -> bool:
    """Return whether the game record is possible given the constraint."""
    obs = summarize_color_observations(
        parse_game_record(record)
    )
    cons = summarize_color_observations(
        parse_constraint(constraint)
    )

    for (color, count) in obs.items():
        if color not in cons:
            return False
        if count > cons[color]:
            return False
        cons[color] -= count
    return True


def main() -> int:
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")[:-1]
    constraint = "12 red cubes, 13 green cubes, 14 blue cubes"
    number_pattern = re.compile(r'Game (\d+):')

    breakpoint()
    part_1 = 0
    for line in lines:
        game_number = int(number_pattern.match(line).groups(1)[0])
        possible = game_is_possible(line, constraint)
        if possible:
            print(game_number)
            part_1 += game_number
    print(f"{part_1=}")

    """
    part_2 = 0
    for line in lines:
        l = replace_words_with_digits(line)
        part_2 += get_calibration_value(l)
    print(f"{part_2=}")
    """

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
