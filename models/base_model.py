#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        Sets the instance attributes if, created_at,
        and updated_at.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel
        instance.
        """

        class_name = self.__class__.__name__
        instance_id = self.id
        instance_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, instance_id, instance_dict)

    def save(self):
        """
        Updates the updated_at, attribute with the cuurent
        datetime.
        calls save() method of storage.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
