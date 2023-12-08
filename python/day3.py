import re
from calendar import c

from pydantic import BaseModel
from utils import read_data


class GridParser(BaseModel):
    """Parses the grid for part numbers"""

    data: list[str]
    candidate_symbols: list[str] = ["#", "+", "*", "$", "@", "/", "^", "&", "%", "!"]

    @property
    def grid(self) -> list[list[str]]:
        """Returns the grid as a list of lists."""
        return [list(line) for line in self.data]

    def extract_digits(self, x: int, y: int) -> str:
        """Concatenates neighboring digits horizontally for a given x, y coordinate in the grid.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            str: The concatenated digits.
        """
        # TODO - check if the index to the left and right is a digit
        # TODO - parse digits to either side of y coordinate and concatenate into a number
        # TODO - make sure resulting numbers are not duplicated off of the same indeces
        line = self.grid[x]
        start_index = y

        # check if the index to the left and right is a digit
        if line[start_index - 1].isdigit():
            pass

        pass

    @property
    def digit_indices(self) -> list[int]:
        """Extracts the digits from the grid."""

        digit_indices = []
        for line_index, line in enumerate(self.grid):
            for index, value in enumerate(line):
                if value.isdigit():
                    digit_indices.append((line_index, index))

        return digit_indices

    def find_digit_adjecent_symbol_in_grid(self) -> bool:
        """Finds whether a given x, y coordinate from digit_indices has an adjecent symbol
        either vertically, horizontally or diagonally.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """
        candidate_digits = []

        for x, y in self.digit_indices:
            if self.has_adjecent_symbol(x, y):
                candidate_digits.append((x, y))

        return candidate_digits

    def has_adjecent_symbol(self, x: int, y: int) -> bool:
        """Finds whether a given x, y coordinate has an adjecent symbol
        either vertically, horizontally or diagonally.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """

        # Check vertically
        if self.check_vertical(x, y):
            return True

        # Check horizontally
        if self.check_horizontal(x, y):
            return True

        # Check diagonally
        if self.check_diagonal(x, y):
            return True

        return False

    def check_vertical(self, x: int, y: int) -> bool:
        """Checks whether a given x, y coordinate has an adjecent symbol vertically.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """

        # Check vertically
        if x + 1 < len(self.grid):
            if self.grid[x + 1][y] in self.candidate_symbols:
                return True

        if x - 1 >= 0:
            if self.grid[x - 1][y] in self.candidate_symbols:
                return True

        return False

    def check_horizontal(self, x: int, y: int) -> bool:
        """Checks whether a given x, y coordinate has an adjecent symbol horizontally.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """

        # Check horizontally
        if y + 1 < len(self.grid[x]):
            if self.grid[x][y + 1] in self.candidate_symbols:
                return True

        if y - 1 >= 0:
            if self.grid[x][y - 1] in self.candidate_symbols:
                return True

        return False

    def check_diagonal(self, x: int, y: int) -> bool:
        """Checks whether a given x, y coordinate has an adjecent symbol diagonally.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """

        # Check diagonally
        if x + 1 < len(self.grid) and y + 1 < len(self.grid[x]):
            if self.grid[x + 1][y + 1] in self.candidate_symbols:
                return True

        if x + 1 < len(self.grid) and y - 1 >= 0:
            if self.grid[x + 1][y - 1] in self.candidate_symbols:
                return True

        if x - 1 >= 0 and y + 1 < len(self.grid[x]):
            if self.grid[x - 1][y + 1] in self.candidate_symbols:
                return True

        if x - 1 >= 0 and y - 1 >= 0:
            if self.grid[x - 1][y - 1] in self.candidate_symbols:
                return True

        return False

    @property
    def digits(self) -> list[int]:
        """Returns the digits from the grid."""

        candidates = self.find_digit_adjecent_symbol_in_grid()
        print(candidates)
        digits = []

        for x, y in candidates:
            digits.append(self.extract_digits(x, y))

        return digits


if __name__ == "__main__":
    data = read_data("test3")

    test = GridParser(data=data)
    print(test.digits)
    # print([list(line) for line in data])
