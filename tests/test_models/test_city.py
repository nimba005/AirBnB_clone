import unittest
from models.city import City
from models.base_model import BaseModel
import models


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_city(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_attributes(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_city_str_method(self):
        expected_str = "[City] ({}) {}".format(
                self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_city_to_dict_method(self):
        obj_dict = self.city.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_city_save_updates_storage(self):
        with unittest.mock.patch.object(models.storage, 'save') as mock_save:
            self.city.save()
            mock_save.assert_called_once()


if __name__ == '__main__':
    unittest.main()
