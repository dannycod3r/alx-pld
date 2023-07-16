import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class AmenityTestCase(unittest.TestCase):
    """Test case for Amenity class"""

    def test_attributes_initialization(self):
        """Test if Amenity attributes are initialized correctly"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inheritance_from_base_model(self):
        """Test if Amenity class inherits from BaseModel"""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

if __name__ == "__main__":
    unittest.main()
