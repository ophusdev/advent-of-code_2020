import unittest
from day_19 import DayNineteen


class TestDayNineteen(unittest.TestCase):

    def test_part_one(self):

        day = DayNineteen()

        self.assertEqual(day.part_one(), 3348222486398, "Should be 3348222486398")
        self.assertEqual(day.part_two(), 43423343619505, "Should be 43423343619505")


if __name__ == '__main__':
    unittest.main()
