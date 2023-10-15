#!/usr/bin/env python3

"""import modules"""

import unittest
import os
from models.user import User
from models.base_model import BaseModel
import models


class TestUser(unittest.TestCase):
    """unittests for user class"""
    def setUp(self):
        self.user = User()

    def test_user_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_user_str(self):
        expected_str = "[User] ({}) {}".format(
                self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def __str__(self):
        return "[User] ({}) {}".format(self.id, self.__dict__)

    def test_user_save_updates(self):
        with unittest.mock.patch.object(models.storage, 'save') as mock_save:
            self.user.save()
            mock_save.assert_called_once()
