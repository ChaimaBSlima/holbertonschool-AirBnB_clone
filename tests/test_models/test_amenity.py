#!/usr/bin/python3
"""
Module for Amenity class
"""
import os
import models
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Unittests for Amenity."""

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_Amenity_attributes(self):
        test_Amenity = Amenity()
        self.assertEqual(test_Amenity.name, "")

    def test_Amenity_inherits_from_base_model(self):
        test_Amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_Amenity_str_representation(self):
        test_Amenity = Amenity()
        test_Amenity.name = "programming"
        Amenity_str = str(test_Amenity)
        self.assertIn("Amenity", Amenity_str)
        self.assertIn("programming", Amenity_str)

    def test_Amenity_to_dict(self):
        test_Amenity = Amenity()
        test_Amenity.name = "programming"
        test_Amenity.save()
        Amenity_dict = test_Amenity.to_dict()
        self.assertEqual(Amenity_dict['name'], "programming")

    def test_Amenity_instance_creation(self):
        test_Amenity = Amenity(name="programming")
        self.assertEqual(test_Amenity.name, "programming")

    def test_Amenity_instance_to_dict(self):
        test_Amenity = Amenity(name="programming")
        Amenity_dict = test_Amenity.to_dict()
        self.assertEqual(Amenity_dict['name'], "programming")

    def test_Amenity_id(self):
        Amenity1 = Amenity()
        Amenity2 = Amenity()
        self.assertNotEqual(Amenity1.id, Amenity2.id)


if __name__ == "__main__":
    unittest.main()
