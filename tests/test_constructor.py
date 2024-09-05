import unittest
from unittest.mock import Mock
from constructor.main import Constructor
from constructor.task import Task
from constructor.substrate import Substrate

class TestConstructor(unittest.TestCase):
    def setUp(self):
        self.task1 = Mock(spec=Task)
        self.task1.name = "Task 1"
        self.task2 = Mock(spec=Task)
        self.task2.name = "Task 2"
        self.constructor = Constructor("Test Constructor", [self.task1, self.task2])

    def test_can_perform(self):
        self.assertTrue(self.constructor.can_perform(self.task1))
        self.assertTrue(self.constructor.can_perform(self.task2))
        
        unknown_task = Mock(spec=Task)
        unknown_task.name = "Unknown Task"
        self.assertFalse(self.constructor.can_perform(unknown_task))

    def test_perform(self):
        mock_substrate = Mock(spec=Substrate)
        
        self.task1.execute.return_value = True
        self.assertTrue(self.constructor.perform(self.task1, mock_substrate))
        self.task1.execute.assert_called_once_with(mock_substrate)
        
        self.task2.execute.return_value = False
        self.assertFalse(self.constructor.perform(self.task2, mock_substrate))
        self.task2.execute.assert_called_once_with(mock_substrate)
        
        unknown_task = Mock(spec=Task)
        unknown_task.name = "Unknown Task"
        self.assertFalse(self.constructor.perform(unknown_task, mock_substrate))
        unknown_task.execute.assert_not_called()

if __name__ == '__main__':
    unittest.main()