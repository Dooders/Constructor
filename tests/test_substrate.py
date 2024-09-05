import unittest
from constructor.substrate import Substrate, ComplexSubstrate
from constructor.task import Task

class TestSubstrate(unittest.TestCase):
    def setUp(self):
        self.substrate = Substrate("initial", "Test Substrate")

    def test_get_set_property(self):
        self.substrate.set_property("test_prop", "test_value")
        self.assertEqual(self.substrate.get_property("test_prop"), "test_value")
        self.assertIsNone(self.substrate.get_property("non_existent_prop"))

class TestComplexSubstrate(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("Task 1", "A", "B")
        self.task2 = Task("Task 2", "B", "C")
        self.complex_substrate = ComplexSubstrate(
            "A",
            ["A", "B", "C"],
            {("A", "B"): self.task1, ("B", "C"): self.task2}
        )

    def test_can_transition(self):
        self.assertTrue(self.complex_substrate.can_transition(self.task1))
        self.assertFalse(self.complex_substrate.can_transition(self.task2))

    def test_perform_transition(self):
        self.assertTrue(self.complex_substrate.perform_transition(self.task1))
        self.assertEqual(self.complex_substrate.current_state, "B")
        
        self.assertTrue(self.complex_substrate.perform_transition(self.task2))
        self.assertEqual(self.complex_substrate.current_state, "C")
        
        self.assertFalse(self.complex_substrate.perform_transition(self.task1))
        self.assertEqual(self.complex_substrate.current_state, "C")

if __name__ == '__main__':
    unittest.main()