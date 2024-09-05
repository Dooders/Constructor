import unittest
from constructor.principle import Principle
from constructor.task import Task

class TestPrinciple(unittest.TestCase):
    def test_principle_is_satisfied(self):
        # Create a principle that always returns True
        always_true = Principle("Always True", lambda t, *args: True)
        mock_task = Task("Mock Task", "input", "output")
        self.assertTrue(always_true.is_satisfied(mock_task))
        
        # Create a principle that always returns False
        always_false = Principle("Always False", lambda t, *args: False)
        self.assertFalse(always_false.is_satisfied(mock_task))
        
        # Create a principle that checks the task name
        name_check = Principle("Name Check", lambda t, *args: t.name == "Correct Name")
        self.assertFalse(name_check.is_satisfied(mock_task))
        mock_task.name = "Correct Name"
        self.assertTrue(name_check.is_satisfied(mock_task))
        
        # Test with additional arguments
        arg_check = Principle("Arg Check", lambda t, *args: len(args) > 0 and args[0] == "correct")
        self.assertFalse(arg_check.is_satisfied(mock_task))
        self.assertTrue(arg_check.is_satisfied(mock_task, "correct"))
        self.assertFalse(arg_check.is_satisfied(mock_task, "incorrect"))

if __name__ == '__main__':
    unittest.main()