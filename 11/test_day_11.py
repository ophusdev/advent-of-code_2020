import unittest
from day_11 import DayEleven


class TestDayEleven(unittest.TestCase):

    def test_part_one(self):

        day_eleven = DayEleven()

        self.assertEqual(day_eleven.part_one(), 2281, "Should be 2281")
        self.assertEqual(day_eleven.part_two(), 2085, "Should be 2085")


if __name__ == '__main__':
    unittest.main()
