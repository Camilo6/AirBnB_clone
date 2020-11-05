#!/usr/bin/python3
'''test state'''

import unittest
import models
import sys
from models.state import State

class test_StateModel(unittest.Testcase):
    """ Test state"""

    def save(self):
        self.model = State()
        self.model.save()

    def test_instance_in_object(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")

if __name__ == "__main__":
    unittest.main()
