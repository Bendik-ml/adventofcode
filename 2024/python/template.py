import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import read_input


def main():
    data = read_input(1)
    print(data)


if __name__ == "__main__":
    main()
