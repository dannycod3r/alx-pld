#!/usr/bin/python3
"""Module contains User test class
"""
import unittest

from models.user import User
from models.base_model import BaseModel

class UserTestCase(unittest.TestCase):
    """Test case for User class"""

    def test_attributes_initialization(self):
        """Test if User attributes are initialized correctly"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance_from_base_model(self):
        """Test if User class inherits from BaseModel"""
        user = User()
        self.assertTrue(isinstance(user, BaseModel))

if __name__ == "__main__":
    unittest.main()
