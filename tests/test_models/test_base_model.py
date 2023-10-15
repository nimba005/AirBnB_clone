#!/usr/bin/env python3

'''Unittests for the BaseModel'''

import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """testmodel testing unittest"""
    def setUp(self):
        self.model = BaseModel()

    def test_instances(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(
                self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)
