import unittest
from models.city import City
from models.base_model import BaseModel

class CityTestCase(unittest.TestCase):
    """Test case for City class"""

    def test_attributes_initialization(self):
        """Test if City attributes are initialized correctly"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance_from_base_model(self):
        """Test if City class inherits from BaseModel"""
        city = City()
        self.assertTrue(isinstance(city, BaseModel))

if __name__ == "__main__":
    unittest.main()
