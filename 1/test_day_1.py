import unittest
from day_1 import DayOne


class TestDayOne(unittest.TestCase):

    def test_part_one(self):

        d_one = DayOne(2020)
        d_one.pair_numbers()

        self.assertEqual(d_one.part_one(), 1007104, "Should be 1007104")

        d_one.tuple_numbers()
        self.assertEqual(d_one.part_two(), 18847752, "Should be 18847752")


if __name__ == '__main__':
    unittest.main()
