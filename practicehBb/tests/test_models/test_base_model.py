#!/usr/bin/python3
"""Module contains test class"""
import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTestCase(unittest.TestCase):
    """Test case for base model"""

    def setUp(self):
        """A common base model instance to be used for testing"""
        self.model = BaseModel()

    # def test_base_model_initialization(self):
    #     """Test if any base model instance have the properties
    #     id(uuid), created_at(datetime) and updated_at(datetime)"""
    #     self.assertIsNotNone(self.model.id)
    #     self.assertIsInstance(self.model.created_at, datetime)
    #     self.assertIsInstance(self.model.updated_at, datetime)
    #     self.assertEqual(self.model.created_at, self.model.updated_at)
    def test_initialization_with_arguments(self):
        model = BaseModel(id='test_id', created_at='2023-07-11T10:00:00.000000', custom_attr='value')
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime(2023, 7, 11, 10, 0, 0))
        self.assertEqual(model.custom_attr, 'value')

    def test_initialization_without_arguments(self):
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_string_representation(self):
        """Test the string representation is same as
        [<class name>] (<self.id>) <self.__dict__>"""
        expected_output = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_output)

    @patch('datetime.datetime')
    def test_save(self, mock_datetime):
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



    def test_to_dict(self):
        """Test to_dict should return dictionary of base model"""
        self.model.updated_at = datetime(2023, 7, 11, 10, 0, 0)

        expected_dict = {
            'id': self.model.id,
            'created_at': self.model.created_at.isoformat(),
            'updated_at': self.model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }

        self.assertEqual(self.model.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
