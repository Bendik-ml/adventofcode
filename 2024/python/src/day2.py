import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import read_input


def is_safe(numbers, dampener=False):
    if len(numbers) < 2:
        return False

    # Check if it's strictly increasing or strictly decreasing
    differences = []
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff == 0:  # Same numbers are not allowed unless dampener is True
            return False
        differences.append(diff)
        print

    # All differences should have the same sign (all positive or all negative)
    if not (all(d > 0 for d in differences) or all(d < 0 for d in differences)):
        return False

    # Check if all differences are between 1 and 3 in absolute value
    return all(1 <= abs(d) <= 3 for d in differences)


def is_safe_with_dampener(numbers):
    # First check if it's already safe without removing any number
    if is_safe(numbers):
        return True

    # Try removing each number and check if the resulting sequence is safe
    for i in range(len(numbers)):
        dampened_sequence = numbers[:i] + numbers[i + 1 :]
        if is_safe(dampened_sequence):
            return True

    return False


def main():
    data = read_input(2, test=False)
    counter = 0

    for line in data:
        numbers = list(map(int, line.split()))
        if is_safe_with_dampener(numbers):
            counter += 1

    return counter


if __name__ == "__main__":
    c = main()
    print(c)
# def main():
#     data = read_input(2, test=False)
#     counter = 0

#     for line in data:
#         # print(l)
#         new_l = list(map(int, line.split()))
#         print(new_l)
#         if sorted(new_l) == new_l:
#             if all([1 <= abs(element) <= 3 for element in np.diff(new_l)]):
#                 print(f"Ascending diff: {np.diff(new_l)}")
#                 counter += 1
#         elif sorted(new_l, reverse=True) == new_l:
#                 if all([1 <= abs(element) <= 2 for element in np.diff(new_l)]):
#                     print(f"Descending diff: {np.diff(new_l)}")
#                     counter += 1
#     return counter


# if __name__ == "__main__":
#     c = main()
#     print(c)
