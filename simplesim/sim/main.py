"""Main Module for the Simple Simulation"""

from random import randint

MIN_POP_START: int = 100
MAX_POP_START: int = 1000
MIN_RESOURCE_START: int = 1000
MAX_RESOURCE_START: int = 10000
MIN_POP_CHANGE: int = 10
MAX_POP_CHANGE: int = 100


class SimpleSimulation:
    """Main Class for the Simulation"""

    def __init__(self, years: int) -> None:
        self.years: int = years
        self.population: int = randint(MIN_POP_START, MAX_POP_START)
        self.resources: int = randint(MIN_RESOURCE_START, MAX_RESOURCE_START)

        self.pop_data: list = []
        self.resource_data: list = []

    def run_sim(self) -> dict:
        """Run the Simulation"""

        for _ in range(self.years):
            self.pop_data.append(self.population)
            self.resource_data.append(self.resources)

            if self.resources == 0:
                break

            pop_change: int = randint(MIN_POP_CHANGE, MAX_POP_CHANGE)
            self.population += pop_change
            self.resources = max(0, self.resources - pop_change)

        return {"pop_data": self.pop_data, "resource_data": self.resource_data}
