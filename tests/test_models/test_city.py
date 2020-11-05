#!/usr/bin/python3
'''test state'''

import unittest
import models
import sys
from models.city import City


class test_CityModel(unittest.Testcase):
    """ Test city """

    def save(self):
        self.model = City()
        self.model.save()

    def test_instance_in_object(self):
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.state_id, "")
        self.assertEqual(self.model.name, "")

if __name__ == "__main__":
    unittest.main()
