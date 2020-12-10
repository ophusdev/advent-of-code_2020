import unittest
from day_10 import DayTen


class TestDayNine(unittest.TestCase):

    def test_part_one(self):

        day_ten = DayTen()

        self.assertEqual(day_ten.part_one(), 1914, "Should be 1914")
        self.assertEqual(day_ten.part_two(), 9256148959232, "Should be 9256148959232")


if __name__ == '__main__':
    unittest.main()
