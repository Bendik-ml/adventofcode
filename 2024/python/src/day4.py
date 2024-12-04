import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import read_input


def main():
    data = read_input(4)
    data = pad_list(data)
    print(data)


def pad_list(data: list):
    return (
        ["." * (len(data[0]) + 8)] * 4
        + ["." * 4 + line + "." * 4 for line in data]
        + ["." * (len(data[0]) + 8)] * 4
    )


if __name__ == "__main__":
    main()
