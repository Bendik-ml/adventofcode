import os
import re
import sys
from ast import literal_eval

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import read_input


def main():
    data = read_input(3)
    parsed = parse_data(data)


def parse_data(data: str):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    candidates = []

    for match in re.finditer(pattern, data):
        if should_include(data, match.start()):
            candidates.append(match.group())

    total = calculate_multiplications(candidates)


def should_include(data: str, start: int):
    preceding_text = data[:start]

    candidate_mentions = list(re.finditer(r"(?:do|don\'t)\(\)", preceding_text))

    if not candidate_mentions:
        return True

    last_match = candidate_mentions[-1].group()

    return last_match == "do()"


def calculate_multiplications(matches: list):
    total = sum(
        x * y for match in matches for x, y in [literal_eval(match.replace("mul", ""))]
    )
    print(total)


if __name__ == "__main__":
    main()
