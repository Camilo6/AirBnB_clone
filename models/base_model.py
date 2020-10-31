#!/usr/bin/python3
""" """


import uuid
from datetime import datetime
import models

format_t = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """ that defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """ args: Not used"""
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, format_t)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        class_name = __class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """ Update datatime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        class_dict = self.__dict__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict