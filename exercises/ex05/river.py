"""File to define River class."""

from exercises.ex05.fish import Fish
from exercises.ex05.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def remove_fish(self, amount: int):
        """Remove amount of Fish from River"""
        for _ in range(0, amount):
            self.fish.pop(_)
        return None

    def check_ages(self):
        """Remove old Fish and Bear's from River"""
        fish: list[Fish] = []
        bears: list[Bear] = []
        i: int = 0
        for fis in self.fish:
            if fis.age <= 10:
                fish.append(fis)
        for bear in self.bears:
            if bear.age <= 10:
                bears.append(bear)
        """Update the river's fish and bears lists"""
        self.fish = fish
        self.bears = bears

        return None

    def bears_eating(self):
        """Simulate Bears eating Fish."""
        for bear in self.bears:
            if len(self.fish) >= 3:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Remove hungry Bears from River"""
        bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bears.append(bear)
        self.bears = bears
        return None

    def repopulate_fish(self):
        """Simulate Fish repopulation"""
        if len(self.fish) >= 2:
            pairs = len(self.fish) // 2 * 4
            for _ in range(0, pairs):
                self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Simulate Bear repopulation"""
        if len(self.bears) >= 2:
            pairs = len(self.bears) // 2
            for _ in range(0, pairs):
                self.bears.append(Bear())

        return None

    def view_river(self):
        print(
            f"""~~~ Day {self.day}: ~~~
        Fish population: {len(self.fish)}
        Bear population: {len(self.bears)}"""
        )
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river"""
        for _ in range(0, 7):
            self.one_river_day()
        return None
