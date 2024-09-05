"""
Substrates are the physical systems or entities upon which tasks are performed. 

Substrates can be thought of as the "materials" that constructors work on to 
produce specific transformations. The role of substrates in Constructor Theory 
is crucial because they are the objects that undergo change when a task is performed.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Tuple

if TYPE_CHECKING:
    from constructor.task import Task

import networkx as nx


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


class ComplexSubstrate:
    def __init__(
        self,
        initial_state: str,
        possible_states: List[str],
        possible_transitions: Dict[Tuple[str, str], "Task"],
    ):
        """
        Initialize a ComplexSubstrate.

        :param initial_state: The starting state of the substrate.
        :param possible_states: List of possible states.
        :param possible_transitions: Dictionary representing possible state transitions (as a graph).
        """
        self.state_graph = nx.DiGraph()
        self.state_graph.add_nodes_from(possible_states)
        for (src, dst), task in possible_transitions.items():
            self.state_graph.add_edge(src, dst, task=task)
        self.current_state = initial_state

    def can_transition(self, task) -> bool:
        """
        Check if the current state can transition using the given task.

        :param task: Task to check.
        :return: True if the transition is possible, False otherwise.
        """
        for neighbor in self.state_graph.neighbors(self.current_state):
            if self.state_graph[self.current_state][neighbor]["task"] == task:
                return True
        return False

    def perform_transition(self, task) -> bool:
        """
        Perform a state transition if possible.

        :param task: Task to perform.
        :return: True if the transition was successful, False otherwise.
        """
        if self.can_transition(task):
            for neighbor in self.state_graph.neighbors(self.current_state):
                if self.state_graph[self.current_state][neighbor]["task"] == task:
                    self.current_state = neighbor
                    return True
        return False
