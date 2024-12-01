from functools import cached_property
from typing import Tuple

from pydantic import BaseModel, computed_field
from utils import read_data

# game cube constraints
CONSTRAINT_RED = 12
CONSTRAINT_BLUE = 14
CONSTRAINT_GREEN = 13


class CubeGame(BaseModel):
    """Represents a game of cube."""

    max_red: int = CONSTRAINT_RED
    max_blue: int = CONSTRAINT_BLUE
    max_green: int = CONSTRAINT_GREEN
    game: str
    max_observed_red: int = 0
    max_observed_blue: int = 0
    max_observed_green: int = 0

    def __init__(self, game: str):
        super().__init__(game=game)
        self.game = game

    @property
    def game_number(self) -> int:
        """Returns the game number."""
        return int(self.game.split(":")[0])

    @property
    def game_outcome(self) -> str:
        """Returns the game outcome."""
        return self.game.split(": ")[1]

    @property
    def number_of_rounds(self) -> int:
        """Returns the number of rounds."""
        return len(self.game_outcome.split("; "))

    @property
    def rounds(self) -> list:
        """Returns the number of rounds."""
        return self.game_outcome.split("; ")

    @property
    def valid_game(self) -> bool:
        """Evaluates the games and checks if the number of red, blue,
        and green cubes exceeds the constraints.
        """

        eval_result = []

        for round in self.rounds:
            for outcome in round.split(", "):
                number_of_cubes = int(outcome.split(" ")[0])
                color_of_cubes = outcome.split(" ")[1].lower()

                if color_of_cubes == "red":
                    eval_result.append(number_of_cubes > self.max_red)
                    if number_of_cubes > self.max_observed_red:
                        self.max_observed_red = number_of_cubes
                elif color_of_cubes == "blue":
                    eval_result.append(number_of_cubes > self.max_blue)
                    if number_of_cubes > self.max_observed_blue:
                        self.max_observed_blue = number_of_cubes
                elif color_of_cubes == "green":
                    eval_result.append(number_of_cubes > self.max_green)
                    if number_of_cubes > self.max_observed_green:
                        self.max_observed_green = number_of_cubes

        if True in eval_result:
            return False
        else:
            return True

    @property
    def power_of_observed_colors(self) -> Tuple[int, int, int]:
        """Returns the power of observed colors."""
        return self.max_observed_red * self.max_observed_blue * self.max_observed_green


def parse_games(data: list[str]) -> list[CubeGame]:
    """Parses the games and returns a list of CubeGame objects."""
    return [CubeGame(game) for game in data]


if __name__ == "__main__":
    data = read_data("day2")

    games = parse_games(data)

    valid_id_list = []
    powers = []

    for game in games:
        if game.valid_game == True:
            valid_id_list.append(game.game_number)

    print(f"Valid games: {sum(valid_id_list)}")

    for game in games:
        powers.append(game.power_of_observed_colors)

    sample = games[0]
    # print(f"Sample game: {sample.game}")
    # print(f"Sample game number: {sample.game_number}")
    # print(f"Sample game outcome: {sample.game_outcome}")
    # print(f"Sample number of rounds: {sample.number_of_rounds}")
    # print(f"Sample rounds: {sample.rounds}")
    # print(f"Sample valid game: {sample.valid_game}")
    # print(f"Sample power of observed colors: {sample.power_of_observed_colors}")
    print(f"sum: {sum(powers)}")
