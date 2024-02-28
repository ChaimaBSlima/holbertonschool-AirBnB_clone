#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel """
    def __init__(self, *args, **kwargs):
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4)
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for i, j in kwargs.items():
                if i == "__class__":
                    continue
                elif i == "updated_at" or i == "updated_at":
                    setattr(self, i, datetime.strptime(j, timeformat))
                else:
                    setattr(self, i, j)

    def save(self):
        """ updated_at take the current datetime."""
        self.updated_at = datetime.utcnow()

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

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
