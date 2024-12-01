import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import read_input

def main():
    return read_input(1)


if __name__ == "__main__":
    main()