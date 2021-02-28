#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""Defines the BaseModel class """


class BaseModel:
    """the BaseModel of the HBnB projectss """

    def __init__(self, *args, **kwargs):
        """Initialize attributes and created, updatede the date"""
        date = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if "created_at" == k:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date)
                elif "updated_at" == k:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date)
                elif "__class__" == k:
                    pass
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string"""
        var3 = self.id
        var4 = self.__dict__
        return ("[{}] {} {}".format(self.__class__.__name__, var3, var4))

    def save(self):
        """save to serialized file"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dic with string formats"""

        dict_1 = self.__dict__.copy()
        dict_1["created_at"] = self.created_at.isoformat()
        dict_1["updated_at"] = self.updated_at.isoformat()
        dict_1["__class__"] = self.__class__.__name__
        return dict_1
