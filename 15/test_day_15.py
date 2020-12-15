import unittest
from day_15 import DayFifteen


class TestDayFifteen(unittest.TestCase):

    def test_part_one(self):

        day = DayFifteen()

        self.assertEqual(day.part_one(2020), 1009, "Should be 1009")
        self.assertEqual(day.part_one(30000000), 62714, "Should be 62714")


if __name__ == '__main__':
    unittest.main()
