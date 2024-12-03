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
    matches = re.findall(pattern, data)
    totals = calculate_multiplications(matches)


def calculate_multiplications(matches: list):
    total = sum(
        x * y for match in matches for x, y in [literal_eval(match.replace("mul", ""))]
    )
    print(total)


if __name__ == "__main__":
    main()
