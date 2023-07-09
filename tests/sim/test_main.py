"""Main Sim Test Module"""

import pytest
from simplesim.sim.main import SimpleSimulation


@pytest.mark.parametrize("years", [(10), (5)])
def test_output_length(years: int):
    """Tests if the sim has output data for the correct number of years"""

    sim: SimpleSimulation = SimpleSimulation(years)
    output: dict = sim.run()
    assert len(output["pop_data"]) == len(output["resource_data"]) == years
