"""
A system is a collection of substrates (physical entities or objects) along with 
their states and properties, which are acted upon by constructors to perform tasks 
(transformations). 

The system represents the overall physical environment or context in which 
transformations happen and can include a variety of components, such as particles, 
objects, fields, and informational entities (like bits or qubits)
"""

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from constructor.substrate import Substrate


class System:
    """
    A system is a collection of substrates

    Attributes
    ----------
    substrates : List[Substrate]
        A list of substrates within the system.
    total_energy : float
        The total energy of the system.

    Methods
    -------
    total_energy() -> float
        Get the total energy of the system.
    update_energy(amount: float) -> None
        Update the total energy of the system.
    update_state(substrate: Substrate, new_state: str) -> None
        Update the state of a substrate within the system.
    """

    def __init__(self, substrates: List["Substrate"], total_energy: float) -> None:
        """
        Initialize a system with substrates and total energy.

        Parameters
        ----------
        substrates : List[Substrate]
            A list of substrates within the system.
        total_energy : float
            The total energy of the system.
        """
        self.substrates = substrates
        self.total_energy = total_energy

    def total_energy(self) -> float:
        """
        Get the total energy of the system.

        Returns
        -------
        float
            The total energy of the system.
        """
        return self.total_energy

    def update_energy(self, amount: float) -> None:
        """
        Update the total energy of the system.

        Parameters
        ----------
        amount : float
            The amount to update the total energy by.
        """
        self.total_energy += amount

    def update_state(self, substrate: "Substrate", new_state: str) -> None:
        """
        Update the state of a substrate within the system.

        Parameters
        ----------
        substrate : Substrate
            The substrate to update.
        new_state : str
            The new state of the substrate.
        """
        for s in self.substrates:
            if s == substrate:
                s.state = new_state
