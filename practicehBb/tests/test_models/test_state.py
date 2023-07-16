import unittest
from models.state import State
from models.base_model import BaseModel

class StateTestCase(unittest.TestCase):
    """Test case for State class"""

    def test_name_initialization(self):
        """Test if State name attribute is initialized correctly"""
        state = State()
        self.assertEqual(state.name, "")

    def test_inheritance_from_base_model(self):
        """Test if State class inherits from BaseModel"""
        state = State()
        self.assertTrue(isinstance(state, BaseModel))

if __name__ == "__main__":
    unittest.main()
