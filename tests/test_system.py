import unittest
from constructor.system import System
from constructor.substrate import Substrate

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.substrate1 = Substrate("state1", "Substrate 1")
        self.substrate2 = Substrate("state2", "Substrate 2")
        self.system = System([self.substrate1, self.substrate2], 100.0)

    def test_total_energy(self):
        self.assertEqual(self.system.total_energy(), 100.0)

    def test_update_energy(self):
        self.system.update_energy(50.0)
        self.assertEqual(self.system.total_energy(), 150.0)
        
        self.system.update_energy(-25.0)
        self.assertEqual(self.system.total_energy(), 125.0)

    def test_update_state(self):
        self.system.update_state(self.substrate1, "new_state")
        self.assertEqual(self.substrate1.state, "new_state")
        self.assertEqual(self.substrate2.state, "state2")  # Unchanged

        # Test updating a substrate not in the system (should have no effect)
        new_substrate = Substrate("state3", "New Substrate")
        self.system.update_state(new_substrate, "new_state")
        self.assertEqual(new_substrate.state, "state3")  # Unchanged

if __name__ == '__main__':
    unittest.main()