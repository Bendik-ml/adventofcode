import os
from typing import List


def read_input(day: int, test: bool = False) -> List[str]:
    suffix = "_test" if test else ""
    file_path = os.path.join(
        os.path.dirname(__file__), "..", "data", f"day{str(day)+suffix}.txt"
    )
    with open(file_path, "r") as file:
        return file.readlines()
