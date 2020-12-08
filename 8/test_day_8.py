import unittest
from day_8 import DayEight


class TestDaySeven(unittest.TestCase):

    def test_part_one(self):

        day_eight = DayEight()

        day_eight.part_one(0)

        self.assertEqual(day_eight.accumulator, 1548, "Should be 1548")
        self.assertEqual(day_eight.accumulator, 1375, "Should be 1375")


if __name__ == '__main__':
    unittest.main()
