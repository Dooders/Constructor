import unittest
from unittest.mock import Mock
from constructor.condition import Condition
from constructor.substrate import Substrate

class TestCondition(unittest.TestCase):
    def test_condition_check(self):
        # Create a mock substrate
        mock_substrate = Mock(spec=Substrate)
        
        # Create a condition that always returns True
        always_true = Condition("Always True", lambda s: True)
        self.assertTrue(always_true.check(mock_substrate))
        
        # Create a condition that always returns False
        always_false = Condition("Always False", lambda s: False)
        self.assertFalse(always_false.check(mock_substrate))
        
        # Create a condition that checks a specific property
        has_property = Condition("Has Property", lambda s: s.get_property("test") == "value")
        mock_substrate.get_property.return_value = "value"
        self.assertTrue(has_property.check(mock_substrate))
        mock_substrate.get_property.return_value = "wrong"
        self.assertFalse(has_property.check(mock_substrate))

if __name__ == '__main__':
    unittest.main()