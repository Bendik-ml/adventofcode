import os
import sys
from collections import Counter

import numpy as np

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import read_input


def main():
    data = read_input(1)
    x, y = [], []
    for line in data:
        left, right = line.split("   ")
        x.append(int(left))
        y.append(int(right))
    x_sorted = sorted(x)
    y_sorted = sorted(y)

    distance = abs(np.array(x_sorted) - np.array(y_sorted))
    sc = calculate_similarity_score(x_sorted, y_sorted)
    print(sum(distance))
    print(sc)
    # print(np.array(sorted(x)))


def calculate_similarity_score(x, y):
    score = 0
    y_counter = Counter(y)

    for element in x:
        score += y_counter[element] * element

    return score


if __name__ == "__main__":
    main()
