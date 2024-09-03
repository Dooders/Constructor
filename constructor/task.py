"""
A task is a physical transformation that could occur, such as converting one state of a system 
into another. In Constructor Theory, tasks are not tied to time; instead, the focus is on 
whether a task can be achieved at all.
"""

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from constructor.condition import Condition
    from constructor.substrate import Substrate


class Task:
    """
    A task is an abstract description of a transformation that can be performed on a substrate.

    Attributes
    ----------
    name: str
        Name of the task.
    input_state: str
        The initial state before transformation.
    output_state: str
        The resulting state after transformation.
    conditions: List[Condition]
        Optional conditions that must be met for the task to be performed.

    Methods
    -------
    is_possible(substrate: Substrate) -> bool
        Check if the task can be performed on the given substrate.
    execute(substrate: Substrate) -> bool
        Perform the task on the substrate, changing its state if possible.
    """

    def __init__(
        self,
        name: str,
        input_state: str,
        output_state: str,
        conditions: List["Condition"] = None,
    ) -> None:
        """
        Initialize a Task.

        Parameters
        ----------
        name: str
            Name of the task.
        input_state: str
            The initial state before transformation.
        output_state: str
            The resulting state after transformation.
        conditions: List[Condition]
            Optional conditions that must be met for the task to be performed.
        """
        self.name = name
        self.input_state = input_state
        self.output_state = output_state
        self.conditions = conditions if conditions else []

    def is_possible(self, substrate: "Substrate") -> bool:
        """
        Check if the task can be performed on the given substrate.

        Parameters
        ----------
        substrate: Substrate
            The substrate on which the task is to be performed.

        Returns
        -------
        bool
            True if the task can be performed, False otherwise.
        """
        if substrate.state == self.input_state:
            return all(condition.check(substrate) for condition in self.conditions)
        return False

    def execute(self, substrate: "Substrate") -> bool:
        """
        Perform the task on the substrate, changing its state if possible.

        Parameters
        ----------
        substrate: Substrate
            The substrate to transform.

        Returns
        -------
        bool
            True if the task was successfully performed, False otherwise.
        """
        if self.is_possible(substrate):
            substrate.state = self.output_state
            return True
        return False
