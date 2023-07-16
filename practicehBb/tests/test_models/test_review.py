import unittest
from models.review import Review
from models.base_model import BaseModel

class ReviewTestCase(unittest.TestCase):
    """Test case for Review class"""

    def test_attributes_initialization(self):
        """Test if Review attributes are initialized correctly"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance_from_base_model(self):
        """Test if Review class inherits from BaseModel"""
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))

if __name__ == "__main__":
    unittest.main()
