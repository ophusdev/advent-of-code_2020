import unittest
from day_4 import DayFour


class TestDayFour(unittest.TestCase):

    def test_part_one(self):

        day_four = DayFour()

        self.assertEqual(day_four.part_one(), 206, "Should be 206")
        self.assertEqual(day_four.part_two(), 123, "Should be 123")


if __name__ == '__main__':
    unittest.main()
