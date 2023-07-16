import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all_returns_dict(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    # def test_new_adds_object_to_objects(self):
    #     model = BaseModel()
    #     self.storage.new(model)
    #     self.assertIn("BaseModel.{}".format(model.id), self.storage.__objects)

    def test_save_serializes_objects_to_file(self):
        model = BaseModel()
        self.storage.new(model)

        with patch("builtins.open", create=True) as mock_open:
            self.storage.save()
            mock_open.assert_called_once_with(self.storage.__class__.__file_path, "w")
            mock_open.return_value.__enter__.return_value.write.assert_called_once()

    # def test_reload_deserializes_file_to_objects(self):
    #     model = BaseModel()
    #     self.storage.new(model)

    #     with patch("builtins.open", create=True) as mock_open:
    #         mock_open.return_value.__enter__.return_value.read.return_value = """
    #         {
    #             "BaseModel.{}": {{
    #                 "id": "{}",
    #                 "created_at": "2023-07-11T10:00:00.000000",
    #                 "updated_at": "2023-07-11T10:00:00.000000",
    #                 "__class__": "BaseModel"
    #             }}
    #         }
    #         """.format(model.id, model.id)

    #         self.storage.reload()
    #         objects = self.storage.all()
    #         self.assertEqual(len(objects), 1)
    #         self.assertIn("BaseModel.{}".format(model.id), objects)

    # def test_reload_handles_file_not_found(self):
    #     with patch("builtins.open", side_effect=FileNotFoundError):
    #         self.storage.reload()


if __name__ == "__main__":
    unittest.main()
