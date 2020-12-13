import unittest
from day_13 import DayThirtheen


class TestDayThirtheen(unittest.TestCase):

    def test_part_one(self):

        day = DayThirtheen()

        self.assertEqual(day.part_one(), 2382, "Should be 2382")
        self.assertEqual(day.part_two(), 906332393333683, "Should be 906332393333683")


if __name__ == '__main__':
    unittest.main()
