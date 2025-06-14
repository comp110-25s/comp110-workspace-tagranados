"""File to define Bear class."""


class Bear:

    age: int
    hunger_score: int

    def __init__(self, age: int = 0, hunger_score: int = 0):
        """New Bear with age and hunger_score 0."""
        return None

    def one_day(self):
        """Simulate one day for Bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Eat num_fish."""
        self.hunger_score += num_fish
        return None
