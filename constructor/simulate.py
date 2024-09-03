"""
Simulations are used to explore the behavior of constructors and substrates.
"""

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from constructor.main import Constructor
    from constructor.substrate import Substrate
    from constructor.task import Task


class Simulation:
    """
    A simulation is used to explore the behavior of constructors and substrates.

    Attributes
    ----------
    constructors: List[Constructor]
        List of Constructor objects.
    substrates: List[Substrate]
        List of Substrate objects.
    tasks: List[Task]
        List of Task objects.

    Methods
    -------
    run() -> None
        Run the simulation, applying constructors to substrates according to their tasks.
    """

    def __init__(
        self,
        constructors: List["Constructor"],
        substrates: List["Substrate"],
        tasks: List["Task"],
    ) -> None:
        """
        Initialize the simulation environment.

        Parameters
        ----------
        constructors: List[Constructor]
            List of Constructor objects.
        substrates: List[Substrate]
            List of Substrate objects.
        tasks: List[Task]
            List of Task objects.
        """
        self.constructors = constructors
        self.substrates = substrates
        self.tasks = tasks

    def run(self) -> None:
        """
        Run the simulation, applying constructors to substrates according to their tasks.
        """
        for substrate in self.substrates:
            for constructor in self.constructors:
                for task in self.tasks:
                    if constructor.perform(task, substrate):
                        print(
                            f"{constructor.name} successfully performed {task.name} on {substrate.name}"
                        )
                    else:
                        print(
                            f"{constructor.name} could not perform {task.name} on {substrate.name}"
                        )
