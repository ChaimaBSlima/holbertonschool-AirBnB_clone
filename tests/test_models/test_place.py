#!/usr/bin/python3
"""
Module for Place class
"""
import os
import models
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unittests for Place."""

    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_Place_attributes(self):
        test_Place = Place()
        self.assertEqual(test_Place.city_id, "")
        self.assertEqual(test_Place.user_id, "")
        self.assertEqual(test_Place.name, "")
        self.assertEqual(test_Place.description, "")
        self.assertEqual(test_Place.number_rooms, 0)
        self.assertEqual(test_Place.number_bathrooms, 0)
        self.assertEqual(test_Place.max_guest, 0)
        self.assertEqual(test_Place.price_by_night, 0)
        self.assertEqual(test_Place.latitude, 0.0)
        self.assertEqual(test_Place.longitude, 0.0)
        self.assertEqual(test_Place.amenity_ids, [])

    def test_Place_inherits_from_base_model(self):
        test_Place = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_Place_str_representation(self):
        test_Place = Place()
        test_Place.city_id = "Sfax"
        test_Place.user_id = "Chaima"
        test_Place.name = " Chaima Hotel "
        test_Place.description = " A five start halel hotel "
        test_Place.number_rooms = 25
        test_Place.number_bathrooms = 25
        test_Place.max_guest = 50
        test_Place.price_by_night = 120
        test_Place.latitude = 10.5
        test_Place.longitude = 15.25
        test_Place.amenity_ids = ["Programming", "writing"]
        self.assertIn("Sfax", str(test_Place.city_id))
        self.assertIn("Chaima", str(test_Place.user_id))
        self.assertIn(" Chaima Hotel ", str(test_Place.name))
        self.assertIn(" A five start halel hotel ",
                      str(test_Place.description))
        self.assertIn(25, int(test_Place.number_rooms))
        self.assertIn(25, int(test_Place.number_bathrooms))
        self.assertIn(50, int(test_Place.max_guest))
        self.assertIn(120, int(test_Place.price_by_night))
        self.assertIn(10.5, float(test_Place.latitude))
        self.assertIn(15.25, float(test_Place.longitude))
        self.assertIn(["Programming", "writing"],
                      list(test_Place.amenity_ids))

    def test_Place_to_dict(self):
        test_Place = Place()
        test_Place.city_id = "Sfax"
        test_Place.user_id = "Chaima"
        test_Place.name = " Chaima Hotel "
        test_Place.description = " A five start halel hotel "
        test_Place.number_rooms = 25
        test_Place.number_bathrooms = 25
        test_Place.max_guest = 50
        test_Place.price_by_night = 120
        test_Place.latitude = 10.5
        test_Place.longitude = 15.25
        test_Place.amenity_ids = ["Programming", "writing"]
        test_Place.save()
        Place_dict = test_Place.to_dict()
        self.assertEqual(Place_dict['city_id '], "Sfax")
        self.assertEqual(Place_dict['user_id'], "Chaima")
        self.assertEqual(Place_dict['name'], " Chaima Hotel ")
        self.assertEqual(Place_dict['description'],
                         " A five start halel hotel ")
        self.assertEqual(Place_dict['number_rooms'], 25)
        self.assertEqual(Place_dict['number_bathrooms'], 25)
        self.assertEqual(Place_dict['max_guest'], 50)
        self.assertEqual(Place_dict['price_by_night'], 120)
        self.assertEqual(Place_dict['latitude'], 10.5)
        self.assertEqual(Place_dict['longitude'], 15.25)
        self.assertEqual(Place_dict['amenity_ids'],
                         ["Programming", "writing"])

    def test_Place_instance_creation(self):
        test_Place = Place(city_id="Sfax", user_id="Chaima",
                           name=" Chaima Hotel ",
                           description=" A five start halel hotel ",
                           number_rooms=25, number_bathrooms=25,
                           max_guest=50, price_by_night=120,
                           latitude=10.5, longitude=15.25,
                           amenity_ids=["Programming", "writing"])
        self.assertEqual(test_Place.city_id, "Sfax")
        self.assertEqual(test_Place.user_id, "Chaima")
        self.assertEqual(test_Place.name, " Chaima Hotel ")
        self.assertEqual(test_Place.description, " A five start halel hotel ")
        self.assertEqual(test_Place.number_rooms, 25)
        self.assertEqual(test_Place.number_bathrooms, 25)
        self.assertEqual(test_Place.max_guest, 50)
        self.assertEqual(test_Place.price_by_night, 120)
        self.assertEqual(test_Place.latitude, 10.5)
        self.assertEqual(test_Place.longitude, 15.25)
        self.assertEqual(test_Place.amenity_ids, ["Programming", "writing"])

    def test_Place_instance_to_dict(self):
        test_Place = Place(city_id="Sfax", user_id="Chaima",
                           name=" Chaima Hotel ",
                           description=" A five start halel hotel ",
                           number_rooms=25, number_bathrooms=25,
                           max_guest=50, price_by_night=120,
                           latitude=10.5, longitude=15.25,
                           amenity_ids=["Programming", "writing"])
        Place_dict = test_Place.to_dict()
        self.assertEqual(Place_dict['city_id '], "Sfax")
        self.assertEqual(Place_dict['user_id'], "Chaima")
        self.assertEqual(Place_dict['name'], " Chaima Hotel ")
        self.assertEqual(Place_dict['description'],
                         " A five start halel hotel ")
        self.assertEqual(Place_dict['number_rooms'], 25)
        self.assertEqual(Place_dict['number_bathrooms'], 25)
        self.assertEqual(Place_dict['max_guest'], 50)
        self.assertEqual(Place_dict['price_by_night'], 120)
        self.assertEqual(Place_dict['latitude'], 10.5)
        self.assertEqual(Place_dict['longitude'], 15.25)
        self.assertEqual(Place_dict['amenity_ids'], ["Programming", "writing"])

    def test_Place_id(self):
        Place1 = Place()
        Place2 = Place()
        self.assertNotEqual(Place1.id, Place2.id)


if __name__ == "__main__":
    unittest.main()
