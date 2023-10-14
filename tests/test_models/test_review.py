#!/usr/bin/python3

"""import modules"""

import unittest
from models.review import Review
from models.base_model import BaseModel
import models


class TestReview(unittest.TestCase):
    """unittetests for review class"""
    def setUp(self):
        self.review = Review()

    def test_review_inheritance(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_attributes_default_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_save_updates_storage(self):
        with unittest.mock.patch.object(models.storage, 'save') as mock_save:
            self.review.save()
            mock_save.assert_called_once()
