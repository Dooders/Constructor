"""
These are the physical systems on which tasks operate. Substrates undergo 
transformations according to the tasks performed by constructors.
"""

from typing import Any


class Substrate:
    """
    A substrate is the object or system on which a task is performed.

    Attributes
    ----------
    state: str
        The current state of the substrate.
    properties: dict
        A dictionary of physical properties of the substrate.

    Methods
    -------
    get_property(name: str) -> Any
        Get a property of the substrate.
    set_property(name: str, value: Any) -> None
        Set a property of the substrate.
    """

    def __init__(self, state: str, name: str) -> None:
        """
        Initialize a Substrate.

        Parameters
        ----------
        state: str
            The initial state of the substrate.
        name: str
            Name of the substrate.
        """
        self.state = state
        self.name = name

    def get_property(self, name: str) -> Any:
        """
        Get a property of the substrate.

        Parameters
        ----------
        name: str
            Name of the property.

        Returns
        -------
        The property value, or None if it doesn't exist.
        """
        return self.properties.get(name)

    def set_property(self, name: str, value: Any) -> None:
        """
        Set a property of the substrate.

        Parameters
        ----------
        name: str
            Name of the property.
        value: Any
            Value to set the property to.
        """
        self.properties[name] = value
