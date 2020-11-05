#!/usr/bin/python3
'''test amenity '''

import unittest
import models
import sys
from models.amenity import Amenity


class test_AmenityModel(unittest.Testcase):
    """ Test amenity """

    def save(self):
        """ Test Save """
        self.model = Amenity()
        self.model.save()

    def test_instance_in_object(self):
        """ Test instances"""
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")

if __name__ == "__main__":
    unittest.main()
