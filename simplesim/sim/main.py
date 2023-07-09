"""Main Module for the Simple Simulation"""

from random import randint
import sys

MIN_POP_START: int = 100
MAX_POP_START: int = 1000
MIN_RESOURCE_START: int = 1000
MAX_RESOURCE_START: int = 10000
MIN_POP_CHANGE: int = 10
MAX_POP_CHANGE: int = 100


class SimpleSimulation:
    """Main Class for the Simulation"""

    def __init__(
        self,
        years: int,
        min_pop_start: int = MIN_POP_START,
        max_pop_start: int = MAX_POP_START,
        min_resource_start: int = MIN_RESOURCE_START,
        max_resource_start: int = MAX_RESOURCE_START,
    ) -> None:
        self.years: int = years
        self.population: int = randint(min_pop_start, max_pop_start)
        self.resources: int = randint(min_resource_start, max_resource_start)

        self.pop_data: list = []
        self.resource_data: list = []

    def run(
        self, min_pop_change: int = MIN_POP_CHANGE, max_pop_change: int = MAX_POP_CHANGE
    ) -> dict:
        """Run the Simulation"""

        for _ in range(self.years):
            self.pop_data.append(self.population)
            self.resource_data.append(self.resources)

            if self.resources == 0:
                break

            pop_change: int = randint(min_pop_change, max_pop_change)
            self.population += pop_change
            self.resources = max(0, self.resources - pop_change)

        return {"pop_data": self.pop_data, "resource_data": self.resource_data}


if __name__ == "__main__":
    sim = SimpleSimulation(int(sys.argv[1]))

    ## TODO: Do something with this data
    output = sim.run()
