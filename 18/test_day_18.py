import unittest
from day_18 import DayEighteen


class TestDayEighteen(unittest.TestCase):

    def test_part_one(self):

        day = DayEighteen()

        self.assertEqual(day.part_one(), 3348222486398, "Should be 3348222486398")
        self.assertEqual(day.part_two(), 43423343619505, "Should be 43423343619505")


if __name__ == '__main__':
    unittest.main()
