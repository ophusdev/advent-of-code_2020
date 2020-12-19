import unittest
from day_19 import DayNineteen


class TestDayNineteen(unittest.TestCase):

    def test_part_one(self):

        day = DayNineteen()

        self.assertEqual(day.part_one(), 265, "Should be 265")
        self.assertEqual(day.part_two(), None, "Should be None")


if __name__ == '__main__':
    unittest.main()
