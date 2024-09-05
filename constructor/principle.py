"""
Principles are rules or constraints that govern which tasks are possible or impossible. 

These principles provide a high-level abstraction of physical laws and govern the 
transformations that constructors can perform on substrates.
"""

from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from constructor.task import Task


class Principle:
    """
    A principle is a rule or constraint that governs which tasks are possible
    or impossible.

    Attributes
    ----------
    name : str
        The name of the principle.
    check_function : Callable[[Any], bool]
        A function that checks if the task satisfies the principle.

    Methods
    -------
    is_satisfied(task: "Task", *args: Any) -> bool
        Check if the task satisfies the principle.
    """

    def __init__(self, name: str, check_function: Callable[[Any], bool]) -> None:
        """
        Initialize a principle that imposes constraints on tasks.

        Parameters
        ----------
        name : str
            The name of the principle.
        check_function : Callable[[Any], bool]
            A function that checks if the task satisfies the principle.
        """
        self.name = name
        self.check_function = check_function

    def is_satisfied(self, task: "Task", *args: Any) -> bool:
        """
        Check if the task satisfies the principle.

        Parameters
        ----------
        task : Task
            The task to check.
        args : Any, optional
            Additional arguments required for the check.

        Returns
        -------
        bool
            True if the principle is satisfied, False otherwise.
        """
        return self.check_function(task, *args)
