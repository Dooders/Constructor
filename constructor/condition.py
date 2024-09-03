"""
In Constructor Theory, conditions are constraints or prerequisites that must be 
satisfied for a task to be executed. 

Conditions determine whether a task is possible given the state of the substrate, 
the properties of the environment, or other factors. They play a crucial role in 
defining the feasibility of transformations within a physical system.
"""

from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from constructor.substrate import Substrate


class Condition:
    """
    A condition is a requirement that must be met for a task to be performed.

    Attributes
    ----------
    name: str
        Name of the condition.
    check_function: Callable[[Substrate], bool]
        A function that returns True if the condition is met, False otherwise.

    Methods
    -------
    check(substrate: Substrate) -> bool
        Check the condition against a substrate.
    """

    def __init__(
        self, name: str, check_function: Callable[["Substrate"], bool]
    ) -> None:
        """
        Initialize a Condition.

        Parameters
        ----------
        name: str
            Name of the condition.
        check_function: Callable[[Substrate], bool]
            A function that returns True if the condition is met, False otherwise.
        """
        self.name = name
        self.check_function = check_function

    def check(self, substrate: "Substrate") -> bool:
        """
        Check the condition against a substrate.

        Parameters
        ----------
        substrate: Substrate
            The substrate to check.

        Returns
        -------
        bool
            True if the condition is met, False otherwise.
        """
        return self.check_function(substrate)
