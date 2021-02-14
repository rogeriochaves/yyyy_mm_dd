import unittest

from yyyy_mm_dd import *

class YYYYMMDDTests(unittest.TestCase):
    def test_move(self):
        self.assertEqual(move_yyyy("2020-02-14", 1), "2021-02-14")
        self.assertEqual(move_yyyy_mm("2020-02-14", 1), "2020-03-14")
        self.assertEqual(move_yyyy_mm_dd("2020-02-29", 1), "2020-03-01")