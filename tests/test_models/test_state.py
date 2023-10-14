#!/usr/bin/python3

"""import module"""

import unittest
from models.state import State
from models.base_model import BaseModel
import models

class TestState(unittest.TestCase):
    """unittests for state class"""
    def setUp(self):
        self.state = State()

    def test_state_inheritance(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_state_str_method(self):
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_state_save(self):
        with unittest.mock.patch.object(models.storage, 'save') as mock_save:
            self.state.save()
            mock_save.assert_called_once()

if __name__ == '__main__':
    unittest.main()
