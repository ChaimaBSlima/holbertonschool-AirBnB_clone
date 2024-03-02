#!/usr/bin/python3
"""
Module for User class
"""
import os
import models
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for User."""

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def test_user_inherits_from_base_model(self):
        test_user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        test_user = User()
        test_user.email = "chaima@example.com"
        test_user.first_name = "Chaima"
        test_user.last_name = "Ben Slima"
        test_user.password = "password484"
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("chaima@example.com", user_str)
        self.assertIn("Chaima", user_str)
        self.assertIn("Ben Slima", user_str)

    def test_user_to_dict(self):
        test_user = User()
        test_user.email = "chaima@example.com"
        test_user.first_name = "Chaima"
        test_user.last_name = "Ben Slima"
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "chaima@example.com")
        self.assertEqual(user_dict['first_name'], "Chaima")
        self.assertEqual(user_dict['last_name'], "Ben Slima")

    def test_user_to_dict(self):
        test_user = User()
        test_user.email = "chaima@example.com"
        test_user.first_name = "Chaima"
        test_user.last_name = "Ben Slima"
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "chaima@example.com")
        self.assertEqual(user_dict['first_name'], "Chaima")
        self.assertEqual(user_dict['last_name'], "Ben Slima")

    def test_user_instance_creation(self):
        test_user = User(email="chaima@example.com", password="password484",
                         first_name="Chaima", last_name="Ben Slima")
        self.assertEqual(test_user.email, "chaima@example.com")
        self.assertEqual(test_user.password, "password484")
        self.assertEqual(test_user.first_name, "Chaima")
        self.assertEqual(test_user.last_name, "Ben Slima")

    def test_user_instance_to_dict(self):
        test_user = User(email="chaima@example.com", password="password484",
                         first_name="Chaima", last_name="Ben Slima")
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "chaima@example.com")
        self.assertEqual(user_dict['password'], "password484")
        self.assertEqual(user_dict['first_name'], "Chaima")
        self.assertEqual(user_dict['last_name'], "Ben Slima")

    def test_user_id(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)


if __name__ == "__main__":
    unittest.main()
