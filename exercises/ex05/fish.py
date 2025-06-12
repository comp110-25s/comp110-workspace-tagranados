"""File to define Fish class."""


class Fish:

    age: int

    def __init__(self, age: int = 0):
        """New Fish with age 0."""
        return None

    def one_day(self):
        """Simulate one day for Fish."""
        self.age += 1
        return None
