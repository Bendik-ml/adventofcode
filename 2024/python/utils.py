import os
from typing import List, Tuple


def read_input(day: int) -> Tuple[int, List[int]]:
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", f"day{day}.txt")
    with open(file_path, "r") as file:
        return [line.strip() for line in file]
