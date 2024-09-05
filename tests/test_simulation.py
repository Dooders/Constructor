import unittest
from unittest.mock import Mock, patch
from constructor.simulate import Simulation
from constructor.main import Constructor
from constructor.substrate import Substrate
from constructor.task import Task

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.constructor1 = Mock(spec=Constructor)
        self.constructor1.name = "Constructor 1"
        self.constructor2 = Mock(spec=Constructor)
        self.constructor2.name = "Constructor 2"
        
        self.substrate1 = Mock(spec=Substrate)
        self.substrate1.name = "Substrate 1"
        self.substrate2 = Mock(spec=Substrate)
        self.substrate2.name = "Substrate 2"
        
        self.task1 = Mock(spec=Task)
        self.task1.name = "Task 1"
        self.task2 = Mock(spec=Task)
        self.task2.name = "Task 2"
        
        self.simulation = Simulation(
            [self.constructor1, self.constructor2],
            [self.substrate1, self.substrate2],
            [self.task1, self.task2]
        )

    @patch('builtins.print')
    def test_run(self, mock_print):
        self.constructor1.perform.return_value = True
        self.constructor2.perform.return_value = False
        
        self.simulation.run()
        
        # Check that perform was called for each combination
        self.assertEqual(self.constructor1.perform.call_count, 4)
        self.assertEqual(self.constructor2.perform.call_count, 4)
        
        # Check that print was called with the correct messages
        mock_print.assert_any_call("Constructor 1 successfully performed Task 1 on Substrate 1")
        mock_print.assert_any_call("Constructor 1 successfully performed Task 2 on Substrate 1")
        mock_print.assert_any_call("Constructor 1 successfully performed Task 1 on Substrate 2")
        mock_print.assert_any_call("Constructor 1 successfully performed Task 2 on Substrate 2")
        mock_print.assert_any_call("Constructor 2 could not perform Task 1 on Substrate 1")
        mock_print.assert_any_call("Constructor 2 could not perform Task 2 on Substrate 1")
        mock_print.assert_any_call("Constructor 2 could not perform Task 1 on Substrate 2")
        mock_print.assert_any_call("Constructor 2 could not perform Task 2 on Substrate 2")

if __name__ == '__main__':
    unittest.main()