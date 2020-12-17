import unittest
from day_17 import DaySeventeen


class TestDaySeventeen(unittest.TestCase):

    def test_part_one(self):

        day = DaySeventeen()

        self.assertEqual(day.part_one(), 359, "Should be 359")
        self.assertEqual(day.part_two(), 2228, "Should be 2228")


if __name__ == '__main__':
    unittest.main()
