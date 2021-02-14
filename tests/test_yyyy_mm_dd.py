import unittest

from yyyy_mm_dd import *

class YYYYMMDDTests(unittest.TestCase):
    def test_move_yyyy(self):
        self.assertEqual(move_yyyy("2020", 1), "2021")
        self.assertEqual(move_yyyy("2020-02", 1), "2021-02")
        self.assertEqual(move_yyyy("2020-02-14", 1), "2021-02-14")
        self.assertEqual(move_yyyy("2020-02-14T10:20:30", 1), "2021-02-14T10:20:30")

    def test_move_yyyy_mm(self):
        self.assertEqual(move_yyyy_mm("2020-02", 1), "2020-03")
        self.assertEqual(move_yyyy_mm("2020-12-14", 1), "2021-01-14")
        self.assertEqual(move_yyyy_mm("2020-02-14T10:20:30", 1), "2020-03-14T10:20:30")

    def test_move_yyyy_mm_dd(self):
        self.assertEqual(move_yyyy_mm_dd("2020-12-31", 1), "2021-01-01")
        self.assertEqual(move_yyyy_mm_dd("2020-02-29T10:20:30", 1), "2020-03-01T10:20:30")

    def test_move_yyyy_mm_dd_hh(self):
        self.assertEqual(move_yyyy_mm_dd_hh("2020-12-31T23", 1), "2021-01-01T00")
        self.assertEqual(move_yyyy_mm_dd_hh("2020-02-29T10:20:30", 1), "2020-02-29T11:20:30")

    def test_move_yyyy_mm_dd_hh_mm(self):
        self.assertEqual(move_yyyy_mm_dd_hh_mm("2020-12-31T23:59", 1), "2021-01-01T00:00")
        self.assertEqual(move_yyyy_mm_dd_hh_mm("2020-02-29T10:20:30", 1), "2020-02-29T10:21:30")

    def test_move_yyyy_mm_dd_hh_mm_ss(self):
        self.assertEqual(move_yyyy_mm_dd_hh_mm_ss("2020-12-31T23:59:59", 1), "2021-01-01T00:00:00")
        self.assertEqual(move_yyyy_mm_dd_hh_mm_ss("2020-02-29T10:20:30", 1), "2020-02-29T10:20:31")

    def test_move_error_cases(self):
        with self.assertRaises(ValueError) as context:
            move_yyyy("foo", 1)
        self.assertTrue('you should provide at least %Y' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            move_yyyy_mm_dd("2020-01", 1)
        self.assertTrue('you should provide at least %Y-%m-%d' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            move_yyyy_mm_dd("2020-01-01foobar", 1)
        self.assertTrue('unconverted data remains: foobar' in str(context.exception))
