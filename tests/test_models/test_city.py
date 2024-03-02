#!/usr/bin/python3
"""
Module for City class
"""
import os
import models
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unittests for City."""

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_City_attributes(self):
        test_City = City()
        self.assertEqual(test_City.state_id, "")
        self.assertEqual(test_City.name, "")

    def test_City_inherits_from_base_model(self):
        test_City = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_City_str_representation(self):
        test_City = City()
        test_City.state_id = "Economy"
        test_City.name = "Sfax"
        City_str = str(test_City)
        self.assertIn("City", City_str)
        self.assertIn("Economy", City_str)
        self.assertIn("Sfax", City_str)

    def test_City_to_dict(self):
        test_City = City()
        test_City.state_id = "Economy"
        test_City.name = "Sfax"
        test_City.save()
        City_dict = test_City.to_dict()
        self.assertEqual(City_dict['state_id'], "Economy")
        self.assertEqual(City_dict['name'], "Sfax")

    def test_City_instance_creation(self):
        test_City = City(state_id="Economy", name="Sfax")
        self.assertEqual(test_City.state_id, "Economy")
        self.assertEqual(test_City.name, "Sfax")

    def test_City_instance_to_dict(self):
        test_City = City(state_id="Economy", name="Sfax")
        City_dict = test_City.to_dict()
        self.assertEqual(test_City.state_id, "Economy")
        self.assertEqual(test_City.name, "Sfax")

    def test_City_id(self):
        City1 = City()
        City2 = City()
        self.assertNotEqual(City1.id, City2.id)


if __name__ == "__main__":
    unittest.main()
