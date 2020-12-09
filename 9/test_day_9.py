import unittest
from day_9 import DayNine


class TestDayNine(unittest.TestCase):

    def test_part_one(self):

        day_nine = DayNine()

        self.assertEqual(day_nine.part_one(), 31161678, "Should be 31161678")
        self.assertEqual(day_nine.part_two(), 5453868, "Should be 5453868")


if __name__ == '__main__':
    unittest.main()
