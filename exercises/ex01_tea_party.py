"""Simple program to calculate the total cost of a tea party."""

__author__ = "730812747"


def main_planner(guests: int) -> None:
    """Entrypoint for the program."""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


def tea_bags(people: int) -> int:
    """Calculate # of tea bags"""
    return people * 2


def treats(people: int) -> int:
    """Calculate # of treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate total cost"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
