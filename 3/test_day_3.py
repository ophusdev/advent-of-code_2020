import unittest
from day_3 import DayThree


class TestDayThree(unittest.TestCase):

    def test_part_one(self):

        day_three = DayThree()

        self.assertEqual(day_three.part_one(3, 1), 259, "Should be 259")
        self.assertEqual(day_three.part_two([(1,1), (3,1), (5,1), (7,1), (1,2)]), 2224913600, "Should be 2224913600")


if __name__ == '__main__':
    unittest.main()
