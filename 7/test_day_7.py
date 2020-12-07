import unittest
from day_7 import DaySeven


class TestDaySeven(unittest.TestCase):

    def test_part_one(self):

        day_seven = DaySeven()

        day_seven.part_one('shiny gold')

        self.assertEqual(len(day_seven.bags), 257, "Should be 257")
        self.assertEqual(day_seven.part_two('shiny gold'), 1038, "Should be 1038")


if __name__ == '__main__':
    unittest.main()
