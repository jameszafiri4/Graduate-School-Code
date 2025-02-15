"""
@author GK

Unit testing the string reverse function

"""
from pydocsDemo import *
import unittest

class TestStringReverse(unittest.TestCase):
    def test_string_reverse(self):
        self.assertAlmostEqual(string_reverse("abcd"), "dcba")
        self.assertAlmostEqual(string_reverse("12345"), "54321")

