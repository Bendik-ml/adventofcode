from upath import UPath


def read_data(day: str) -> list[str]:
    path = UPath(f"../data/{day}.txt")
    with open((path), "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    print(read_data("day1"))
