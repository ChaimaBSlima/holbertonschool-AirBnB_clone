#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel """
    def __init__(self, *args, **kwargs):
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for i, j in kwargs.items():
                if i == "__class__":
                    continue
                elif i == "updated_at" or i == "created_at":
                    setattr(self, i, datetime.strptime(j, timeformat))
                else:
                    setattr(self, i, j)
        models.storage.new(self)

    def save(self):
        """ updated_at take the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance.
        """
        chaima = self.__dict__.copy()
        chaima["__class__"] = self.__class__.__name__
        chaima["created_at"] = self.created_at.isoformat()
        chaima["updated_at"] = self.updated_at.isoformat()

        return chaima

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
