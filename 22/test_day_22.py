import unittest
from day_22 import DayTwentyTwo


class TestDayTwentyTwo(unittest.TestCase):

    def test_part_one(self):

        day = DayTwentyTwo()

        self.assertEqual(day.part_one(), 33694, "Should be 33694")
        day = DayTwentyTwo()
        self.assertEqual(day.part_two(), 31835, "Should be 31835")


if __name__ == '__main__':
    unittest.main()
