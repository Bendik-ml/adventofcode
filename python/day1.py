import enum
import re

from utils import read_data


class NumberWords(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


def find_and_replace_number_words(string: str) -> str:
    """Finds and replaces number words in a string with their corresponding digits."""
    for digit_enum in NumberWords:
        if digit_enum.name.lower() in string:
            substrings = [
                m.start() for m in re.finditer(digit_enum.name.lower(), string)
            ]

            for substring in substrings:
                string = (
                    string[: substring + 1]
                    + str(digit_enum.value)
                    + string[substring + 2 :]
                )
        else:
            continue
    return string


def collect_digits(string: str) -> list[int]:
    """Collects all digits in a string and returns them as a list."""
    return [int(digit) for digit in string if digit.isdigit()]


def combine_digits(string: str) -> int:
    """Combines the first and last digits of a string and returns the result."""
    reformatted_string = find_and_replace_number_words(string)
    digits = collect_digits(reformatted_string)

    if len(digits) == 0:
        return 0
    elif len(digits) == 1:
        return int("".join([str(digits[0]), str(digits[0])]))
    else:
        return int("".join([str(digits[0]), str(digits[-1])]))


if __name__ == "__main__":
    data = read_data("day1")

    combined_numbers = []
    for string in data:
        combined_numbers.append(combine_digits(string))

    total_sum = sum(combined_numbers)

    print(total_sum)
