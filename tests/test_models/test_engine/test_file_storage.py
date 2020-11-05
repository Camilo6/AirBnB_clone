#!/usr/bin/python3

"""
Unittest for BaseModel
"""

import unittest
from models.base_model import BaseModel


class Test_attributes(unittest.TestCase):
    """ Tests attributes """

    def test_id(self):
        """ test id """

        self.assertEqual(type(self.id), str)

    def test_created_at(self):
        """ test created_at """

        base = BaseModel().to_dict()
        self.assertEqual(type(self.created_at), datetime.datetime)
        self.assertEqual(type(base.created_at), str)

    def test_updated_at(self):
        """ test updated_at """

        base = BaseModel().to_dict()
        self.assertEqual(type(self.updated_at), datetime.datetime)
        self.assertEqual(type(base.updated_at), str)

if __name__ == '__main__':
    unittest.main()
