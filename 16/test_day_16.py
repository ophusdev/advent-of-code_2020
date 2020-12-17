import unittest
from day_16 import DaySixteen


class TestDaySixteen(unittest.TestCase):

    def test_part_one(self):

        day = DaySixteen()

        self.assertEqual(day.part_one(), 23036, "Should be 23036")
        self.assertEqual(day.part_two(), None, "Should be None")


if __name__ == '__main__':
    unittest.main()
