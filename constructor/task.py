"""
A task is a fundamental concept representing a possible transformation or 
operation that can be performed on a substrate. 

A task describes the change from one state to another and is central to 
understanding what is possible or impossible in a given physical system.
"""

from functools import wraps
from typing import TYPE_CHECKING, Callable, List, Union

if TYPE_CHECKING:
    from constructor.condition import Condition
    from constructor.substrate import Substrate


class Task:
    """
    A task is an abstract description of a transformation that can be performed
    on a substrate.

    Attributes
    ----------
    name: str
        Name of the task.
    conditions: List[Condition]
        Optional conditions that must be met for the task to be performed.

    Methods
    -------
    is_possible(substrate: Substrate) -> bool
        Check if the task can be performed on the given substrate.
    execute(substrate: Substrate) -> Union[Substrate, bool]
        Perform the task on the substrate, changing its state if possible.
    """

    def __init__(
        self,
        name: str,
        conditions: List["Condition"] = None,
    ) -> None:
        """
        Initialize a Task.

        Parameters
        ----------
        name: str
            Name of the task.
        conditions: List[Condition]
            Optional conditions that must be met for the task to be performed.
        """
        self.name = name
        self.conditions = conditions

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

        return all(condition.check(substrate) for condition in self.conditions)

    @classmethod
    def execute(cls) -> Callable[["Substrate"], Union["Substrate", bool]]:
        """
        Decorator for task execution to check if the task is possible before
        performing it.

        Returns
        -------
        Callable[["Substrate"], Union["Substrate", bool]]
            A function that performs the task on a substrate.
            Returns the substrate if the task is possible, False otherwise.
        """

        def decorator(substrate: "Substrate", *args) -> Union["Substrate", bool]:
            if cls.is_possible(substrate):
                substrate = cls(substrate, *args)

                return substrate
            else:
                return False

        return decorator
