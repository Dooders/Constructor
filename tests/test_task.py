import unittest
from unittest.mock import Mock
from constructor.task import Task
from constructor.condition import Condition
from constructor.substrate import Substrate

class TestTask(unittest.TestCase):
    def setUp(self):
        self.condition1 = Mock(spec=Condition)
        self.condition2 = Mock(spec=Condition)
        self.task = Task("Test Task", "input_state", "output_state", [self.condition1, self.condition2])
        self.substrate = Mock(spec=Substrate)

    def test_is_possible(self):
        self.substrate.state = "input_state"
        self.condition1.check.return_value = True
        self.condition2.check.return_value = True
        self.assertTrue(self.task.is_possible(self.substrate))
        
        self.condition2.check.return_value = False
        self.assertFalse(self.task.is_possible(self.substrate))
        
        self.substrate.state = "wrong_state"
        self.assertFalse(self.task.is_possible(self.substrate))

    def test_execute(self):
        self.substrate.state = "input_state"
        self.condition1.check.return_value = True
        self.condition2.check.return_value = True
        
        self.assertTrue(self.task.execute(self.substrate))
        self.assertEqual(self.substrate.state, "output_state")
        
        self.substrate.state = "input_state"
        self.condition2.check.return_value = False
        self.assertFalse(self.task.execute(self.substrate))
        self.assertEqual(self.substrate.state, "input_state")  # Unchanged

if __name__ == '__main__':
    unittest.main()