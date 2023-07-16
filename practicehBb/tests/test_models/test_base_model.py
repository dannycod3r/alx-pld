#!/usr/bin/python3
"""Module contains BaseModel test class
"""
import unittest

from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):
    """Test case for base model"""

    def setUp(self):
        """Set up the test ca"""
        self.model = BaseModel()

    def test_initialization_without_arguments(self):
        """Test initialization without keyword argument"""
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_initialization_with_arguments(self):
        """Test initialization with keyword argument"""
        model = BaseModel(
            id='test_id',
            created_at='2023-07-11T10:00:00.000000',
            custom_attr='value'
        )
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime(2023, 7, 11, 10, 0, 0))
        self.assertEqual(model.custom_attr, 'value')

    def test_instance_has_attributes(self):
        """Test if any instance has the attributes
        id, created_at and updated at"""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_is_string(self):
        """Test to ensure id attribute is string"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """Ensure created_at is type datetime"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Ensure updated_at is type datetime"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_string_representation(self):
        """Test the string representation is same as
        [<class name>] (<self.id>) <self.__dict__>"""
        expected_output = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_output)

    @patch('datetime.datetime')
    def test_save_updates_updated_at(self, mock_datetime):
        """Test save method must modify the updated at attribute"""
        mock_now = datetime.now()
        mock_datetime.now.return_value = mock_now

        self.model.save()
        self.assertEqual(
            # microsecond is set to 0 to make test accurate
            # test fails at a point when microseconds differ
            self.model.updated_at.replace(microsecond=0),
            mock_now.replace(microsecond=0)
        )

    def test_to_dict_returns_dict(self):
        """Test to_dict should return dictionary of base model"""
        self.model.updated_at = datetime(2023, 7, 11, 10, 0, 0)

        expected_dict = {
            'id': self.model.id,
            'created_at': self.model.created_at.isoformat(),
            'updated_at': self.model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }

        self.assertEqual(self.model.to_dict(), expected_dict)

    def test_to_dict_has_expected_keys(self):
        """Test if to_dict returns the expected keys"""
        obj_dict = self.model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_to_dict_created_at_format(self):
        """Test the time format for created_at in to_dict"""
        obj_dict = self.model.to_dict()
        created_at = obj_dict['created_at']
        expected_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(datetime.strptime(created_at, expected_format), self.model.created_at)


    def test_to_dict_updated_at_format(self):
        """Test the time format for updated_at in to_dict"""
        self.model.save()
        obj_dict = self.model.to_dict()
        updated_at = obj_dict['updated_at']
        self.assertEqual(
            datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f"), self.model.updated_at)


if __name__ == "__main__":
    unittest.main()
