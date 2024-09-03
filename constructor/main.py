"""
Entities that perform tasks. A constructor can carry out a transformation (task) 
repeatedly without being degraded by it. In a sense, it is an abstract machine 
that causes changes but is not itself changed.
"""

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from constructor.substrate import Substrate
    from constructor.task import Task


class Constructor:
    """
    A constructor is an entity that can perform tasks on substrates.

    Attributes
    ----------
    name: str
        Name of the constructor.
    capabilities: List[Task]
        List of tasks this constructor can perform.

    Methods
    -------
    can_perform(task: Task) -> bool
        Check if the constructor can perform a given task.
    perform(task: Task, substrate: Substrate) -> bool
        Perform a task on a substrate if possible.
    """

    def __init__(self, name: str, capabilities: List["Task"]) -> None:
        """
        Initialize a Constructor.

        Parameters
        ----------
        name: str
            Name of the constructor.
        capabilities: List[Task]
            List of tasks this constructor can perform.
        """
        self.name = name
        self.capabilities = capabilities

    def can_perform(self, task: "Task") -> bool:
        """
        Check if the constructor can perform a given task.

        Parameters
        ----------
        task: Task
            Task object to check.

        Returns
        -------
        bool
            True if the constructor can perform the task, False otherwise.
        """
        return task in self.capabilities

    def perform(self, task: "Task", substrate: "Substrate") -> bool:
        """
        Perform a task on a substrate if possible.

        Parameters
        ----------
        task: Task
            Task to be performed.
        substrate: Substrate
            Substrate on which the task is performed.

        Returns
        -------
        bool
            True if the task was successfully performed, False otherwise.
        """
        if self.can_perform(task):
            return task.execute(substrate)
        else:
            return False
