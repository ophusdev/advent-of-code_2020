import unittest
from day_12 import DayTwelve


class TestDayTwelve(unittest.TestCase):

    def test_part_one(self):

        day_twelve = DayTwelve()

        self.assertEqual(day_twelve.part_one(), 879, "Should be 879")
        self.assertEqual(day_twelve.part_two(), 18107, "Should be 18107")


if __name__ == '__main__':
    unittest.main()
