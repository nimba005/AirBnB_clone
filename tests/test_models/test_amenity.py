#!/usr/bin/python3

"""import modules"""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import models
import datetime


class TestAmenity(unittest.TestCase):
    """instances of a method unittests"""
    am = Amenity()

    def test_class_exists(self):
        """tests if class exists"""
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.am)), result)

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.am.name, str)
        self.assertIsInstance(self.am.id, str)
        self.assertIsInstance(self.am.created_at, datetime.datetime)
        self.assertIsInstance(self.am.updated_at, datetime.datetime)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.am, 'name'))
        self.assertTrue(hasattr(self.am, 'id'))
        self.assertTrue(hasattr(self.am, 'created_at'))
        self.assertTrue(hasattr(self.am, 'updated_at'))
