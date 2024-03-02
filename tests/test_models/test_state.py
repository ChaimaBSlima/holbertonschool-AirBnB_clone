#!/usr/bin/python3
"""
Module for Amenity class
"""
import os
import models
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unittests for Amenity."""

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_State_attributes(self):
        test_State = State()
        self.assertEqual(test_State.name, "")

    def test_State_inherits_from_base_model(self):
        test_State = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_State_str_representation(self):
        test_State = State()
        test_State.name = "Programmer"
        State_str = str(test_State)
        self.assertIn("State", State_str)
        self.assertIn("Programmer", State_str)

    def test_State_to_dict(self):
        test_State = State()
        test_State.name = "Programmer"
        test_State.save()
        State_dict = test_State.to_dict()
        self.assertEqual(State_dict['name'], "Programmer")

    def test_State_instance_creation(self):
        test_State = State(name="Programmer")
        self.assertEqual(test_State.name, "Programmer")

    def test_State_instance_to_dict(self):
        test_State = State(name="Programmer")
        State_dict = test_State.to_dict()
        self.assertEqual(State_dict['name'], "Programmer")

    def test_State_id(self):
        State1 = State()
        State2 = State()
        self.assertNotEqual(State1.id, State2.id)


if __name__ == "__main__":
    unittest.main()
