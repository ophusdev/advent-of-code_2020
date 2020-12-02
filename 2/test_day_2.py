import unittest
from day_2 import DayTwo


class TestDayTwo(unittest.TestCase):

    def test_part_one(self):

        day_two = DayTwo()
        day_two.part_one()

        self.assertEqual(day_two.valid_password, 396, "Should be 396")

        day_two.part_two()
        self.assertEqual(day_two.valid_position, 428, "Should be 428")


if __name__ == '__main__':
    unittest.main()
