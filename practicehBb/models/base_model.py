#!/usr/bin/python3
"""Module contains the base model class
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base model class define all common
    attributes or methods for other classes

    Methods:
        save:  updates the public instance attribute

        to_dict:
    """
    def __init__(self, *args, **kwargs):
        """Class constructor called when object is created

        Args:
            kwargs(any): keyword args

            id(uuid): unique identifier for each instance

            created_at(datetime): time instance is created

            updated_at(datetime): time instance is updated
        """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """A friendly representation of base model

        Format:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance
        attribute updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """return a dictionary containing all key/value
            of __dict__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        if hasattr(self, 'updated_at'):
            obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
