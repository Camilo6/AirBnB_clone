#!/usr/bin/python3
"""
Define: BaseModel class unitests
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unitests.TestCase):

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))


if __name__ == "__main__":
    unittest.main()
