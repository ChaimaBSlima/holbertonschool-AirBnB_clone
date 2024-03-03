#!/usr/bin/python3
"""
testing the base model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_ing_init(self):
        """
        Test for __init__
        """
        chaima = BaseModel()
        self.assertIsNotNone(chaima.id)
        self.assertIsNotNone(chaima.created_at)
        self.assertIsNotNone(chaima.updated_at)

    def test_ing_save(self):
        """
        Test for save
        """
        chaima = BaseModel()
        upat = chaima.updated_at
        cupat = chaima.save()
        self.assertNotEqual(upat, cupat)

    def test_ing_to_dict(self):
        """
        Test for to_dict
        """
        chaima = BaseModel()
        mdict = chaima.to_dict()
        self.assertIsInstance(mdict, dict)
        self.assertEqual(mdict["__class__"], 'BaseModel')
        self.assertEqual(mdict['id'], chaima.id)
        self.assertEqual(mdict['created_at'], chaima.created_at.isoformat())
        self.assertEqual(mdict["updated_at"], chaima.updated_at.isoformat())

    def test_ing_str(self):
        """
        Test for string representation
        """
        chaima = BaseModel()
        self.assertTrue(str(chaima).startswith('[BaseModel]'))
        self.assertIn(chaima.id, str(chaima))
        self.assertIn(str(chaima.__dict__), str(chaima))


if __name__ == "__main__":
    unittest.main()
