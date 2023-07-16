import unittest

from models.place import Place
from models.base_model import BaseModel

class PlaceTestCase(unittest.TestCase):
    """Test case for Place class"""

    def test_attributes_initialization(self):
        """Test if Place attributes are initialized correctly"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance_from_base_model(self):
        """Test if Place class inherits from BaseModel"""
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))

if __name__ == "__main__":
    unittest.main()
