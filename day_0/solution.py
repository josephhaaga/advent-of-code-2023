from typing import Tuple


def example():
    return None


def main() -> int:
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
    for line in lines:
        ...
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
