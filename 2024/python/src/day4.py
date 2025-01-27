import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import read_input


def main(search_string: str = "XMAS"):
    data = read_input(4)
    data = pad_list(data)
    xmas = count_xmas(data, search_string)
    mas = count_mas(data, search_string)
    print(xmas)
    print(mas)


def pad_list(data: list):
    return (
        ["." * (len(data[0]) + 8)] * 4
        + ["." * 4 + line + "." * 4 for line in data]
        + ["." * (len(data[0]) + 8)] * 4
    )


def count_xmas(data: list, target_string: str, makes_cross: bool = False) -> int:
    count = 0
    height = len(data)
    width = len(data[0])
    target_length = len(target_string)

    for x in range(4, height - 4):  # Skip the padding
        for y in range(4, width - 4):  # Skip the padding
            if data[x][y] == ".":
                continue

            # Check horizontal
            word = "".join(data[x][y : y + target_length])
            if target_string in word or target_string in word[::-1]:
                count += 1

            # Check vertical
            word = "".join(data[i][y] for i in range(x, x + target_length))
            if target_string in word or target_string in word[::-1]:
                count += 1

            # Check diagonal (top-left to bottom-right)
            word = "".join(data[x + i][y + i] for i in range(target_length))
            if target_string in word or target_string in word[::-1]:
                count += 1

            # Check diagonal (top-right to bottom-left)
            word = "".join(data[x + i][y - i] for i in range(target_length))
            if target_string in word or target_string in word[::-1]:
                count += 1

    return count


def count_mas(data: list, target_string: str, makes_cross: bool = False) -> int:
    count = 0
    height = len(data)
    width = len(data[0])

    for x in range(4, height - 4):  # Skip the padding
        for y in range(4, width - 4):  # Skip the padding
            if data[x][y] != "M":
                continue

            word1 = "".join(data[x + i][y + i] for i in range(len(target_string)))
            word2 = "".join(data[x + i][y - i] for i in range(len(target_string)))

            if (target_string in word1 or target_string in word1[::-1]) and (
                target_string in word2 or target_string in word2[::-1]
            ):
                count += 1

    return count


if __name__ == "__main__":
    # main("XMAS") # day 1
    main("MAS")  # day 2
