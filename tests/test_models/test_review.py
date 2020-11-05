#!/usr/bin/python3
'''test review'''
import unittest
from models.review import Review

class test_ReviewModel(unittest.Testcase):

    def save(self):
        self.model = Review()
        self.model.save()

    def test_instance_in_object(self):
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")

if __name__ == "__main__":
    unittest.main()
