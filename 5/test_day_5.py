import unittest
from day_5 import DayFive


class TestDayFive(unittest.TestCase):

    def test_part_one(self):

        day_five = DayFive()

        self.assertEqual(day_five.part_one(), 963, "Should be 963")
        self.assertEqual(day_five.part_two()[0], 592, "Should be 592")


if __name__ == '__main__':
    unittest.main()
