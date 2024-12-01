import re
from calendar import c
from curses.ascii import isdigit

from pydantic import BaseModel
from utils import read_data


class GridParser(BaseModel):
    """Parses the grid for part numbers"""

    data: list[str]
    candidate_symbols: list[str] = ["+", "&", "-", "*", "%", "=", "#", "@", "/", "$"]
    candidate_numbers: list[str] = [str(i) for i in range(11)]

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
        row = self.grid[x]
        start_col_index = y

        # check if the index to the left and right is a digit
        if row[start_col_index - 1].isdigit() & row[start_col_index + 1].isdigit():
            return row[start_col_index - 1 : start_col_index + 2]

        # check if the index to the left is a digit
        if row[start_col_index - 1].isdigit():
            if row[start_col_index - 2].isdigit():
                return row[start_col_index - 2 : start_col_index + 1]
            else:
                return row[start_col_index - 1 : start_col_index + 1]

        # check if the index to the right is a digit
        if row[start_col_index + 1].isdigit():
            if row[start_col_index + 2].isdigit():
                return row[start_col_index : start_col_index + 3]
            else:
                return row[start_col_index : start_col_index + 2]

        else:
            return row[start_col_index]

    @property
    def digit_indices(self) -> list[int]:
        """Extracts the digits from the grid."""

        digit_indices = []
        for line_index, line in enumerate(self.grid):
            for index, value in enumerate(line):
                if value.isdigit():
                    digit_indices.append((line_index, index))

        return digit_indices

    @property
    def asterisk_indices(self) -> list[int]:
        """Extracts the digits from the grid."""

        asterisk_indices = []
        for line_index, line in enumerate(self.grid):
            for index, value in enumerate(line):
                if value == "*":
                    asterisk_indices.append((line_index, index))

        return asterisk_indices

    def find_digit_adjecent_symbol_in_grid(self) -> bool:
        """Finds whether a given x, y coordinate from digit_indices has an adjecent symbol
        either vertically, horizontally or diagonally.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """
        candidate_digits = []

        for x, y in self.digit_indices:
            if self.has_adjecent_symbol(x, y, self.candidate_symbols):
                candidate_digits.append((x, y))

        return candidate_digits

    def find_numbers_adjacent_to_symbol(self) -> bool:
        """Finds whether a given x, y coordinate from digit_indices has an adjecent symbol
        either vertically, horizontally or diagonally.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """
        candidate_digits = []

        for x, y in self.asterisk_indices:
            # add a counter. We only coordinates that have atleast 2 digits
            counter = 0 # TODO COUNT UP THE NUMBERS NEXT TO THE ASTERISK AND COLLECT THOSE.
            if self.has_adjecent_symbol(x, y, self.candidate_numbers):
                candidate_digits.append((x, y))

        return candidate_digits

    def has_adjecent_symbol(self, x: int, y: int, search_list: list[str], return_location:bool = False) -> bool:
        """Finds whether a given x, y coordinate has an adjecent symbol
        either vertically, horizontally or diagonally.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """

        # Check vertically
        if self.check_vertical(x, y, search_list):
            return True

        # Check horizontally
        if self.check_horizontal(x, y, search_list):
            return True

        # Check diagonally
        if self.check_diagonal(x, y, search_list):
            return True

        return False

    def check_vertical(self, x: int, y: int, search_list: list[str]) -> bool:
        """Checks whether a given x, y coordinate has an adjecent symbol vertically.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """

        # Check vertically
        if x + 1 < len(self.grid):
            if self.grid[x + 1][y] in search_list:
                return True

        if x - 1 >= 0:
            if self.grid[x - 1][y] in search_list:
                return True

        return False

    def check_horizontal(self, x: int, y: int, search_list: list[str]) -> bool:
        """Checks whether a given x, y coordinate has an adjecent symbol horizontally.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """

        # Check horizontally
        if y + 1 < len(self.grid[x]):
            if self.grid[x][y + 1] in search_list:
                return True

        if y - 1 >= 0:
            if self.grid[x][y - 1] in search_list:
                return True

        return False

    def check_diagonal(self, x: int, y: int, search_list: list[str]) -> bool:
        """Checks whether a given x, y coordinate has an adjecent symbol diagonally.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            bool: True if it has an adjecent symbol, False otherwise.
        """

        # Check diagonally
        if x + 1 < len(self.grid) and y + 1 < len(self.grid[x]):
            if self.grid[x + 1][y + 1] in search_list:
                return True

        if x + 1 < len(self.grid) and y - 1 >= 0:
            if self.grid[x + 1][y - 1] in search_list:
                return True

        if x - 1 >= 0 and y + 1 < len(self.grid[x]):
            if self.grid[x - 1][y + 1] in search_list:
                return True

        if x - 1 >= 0 and y - 1 >= 0:
            if self.grid[x - 1][y - 1] in search_list:
                return True

        return False

    @property
    def digits(self) -> list[int]:
        """Returns the digits from the grid."""

        candidates = self.find_digit_adjecent_symbol_in_grid()
        digit_chars = []

        for x, y in candidates:
            digit_chars.append(self.extract_digits(x, y))

        for k, v in enumerate(candidates[:200]):
            print(k, v)
        joined_digits = [int("".join(char_list)) for char_list in digit_chars]
        filtered_numbers = [
            num
            for num, next_num in zip(joined_digits, joined_digits[1:] + [None])
            if num != next_num
        ]
        return filtered_numbers

    @property
    def gears(self) -> list[int]:
        """Returns the digits neighbouring an asterisk from the grid."""

        candidates = self.find_symbol_adjacent_digit_in_grid()
        digit_chars = []

        for x, y in candidates:
            digit_chars.append(self.extract_digits_around_symbol(x, y))

        return digit_chars
        # joined_digits = [int("".join(char_list)) for char_list in digit_chars]

        # return joined_digits
        # filtered_numbers = [
        #     num
        #     for num, next_num in zip(joined_digits, joined_digits[1:] + [None])
        #     if num != next_num
        # ]
        # return filtered_numbers

    def extract_symbols_
if __name__ == "__main__":
    data = read_data("test3")

    test = GridParser(data=data)
    digits = test.gears
    print(digits)
