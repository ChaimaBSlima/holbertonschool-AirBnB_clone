#!/usr/bin/python3
"""
Module for Review class
"""
import os
import models
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unittests for Review."""

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_Review_attributes(self):
        test_Review = Review()
        self.assertEqual(test_Review.place_id, "")
        self.assertEqual(test_Review.user_id, "")
        self.assertEqual(test_Review.text, "")

    def test_Review_inherits_from_base_model(self):
        test_Review = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_Review_str_representation(self):
        test_Review = Review()
        test_Review.place_id = "Sfax"
        test_Review.user_id = "Chaima"
        test_Review.text = "chaima is a great ML Developper"
        Review_str = str(test_Review)
        self.assertIn("Review", Review_str)
        self.assertIn("Sfax", Review_str)
        self.assertIn("Chaima", Review_str)
        self.assertIn("chaima is a great ML Developper", Review_str)

    def test_Review_to_dict(self):
        test_Review = Review()
        test_Review.place_id = "Sfax"
        test_Review.user_id = "Chaima"
        test_Review.text = "chaima is a great ML Developper"
        test_Review.save()
        Review_dict = test_Review.to_dict()
        self.assertEqual(Review_dict['place_id'], "Sfax")
        self.assertEqual(Review_dict['user_id'], "Chaima")
        self.assertEqual(Review_dict['text'], "chaima is\
                         a great ML Developper")

    def test_Review_instance_creation(self):
        test_Review = Review(place_id="Sfax", user_id="Chaima",
                             text="chaima is a great ML Developper")
        self.assertEqual(test_Review.place_id, "Sfax")
        self.assertEqual(test_Review.user_id, "Chaima")
        self.assertEqual(test_Review.text, "chaima is a great ML Developper")

    def test_Review_instance_to_dict(self):
        test_Review = Review(place_id="Sfax", user_id="Chaima",
                             text="chaima is a great ML Developper")
        Review_dict = test_Review.to_dict()
        self.assertEqual(Review_dict['place_id'], "Sfax")
        self.assertEqual(Review_dict['user_id'], "Chaima")
        self.assertEqual(Review_dict['text'], "chaima is a\
            great ML Developper")

    def test_Review_id(self):
        Review1 = Review()
        Review2 = Review()
        self.assertNotEqual(Review1.id, Review2.id)


if __name__ == "__main__":
    unittest.main()
