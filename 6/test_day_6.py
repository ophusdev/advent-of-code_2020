import unittest
from day_6 import DaySix


class TestDaySix(unittest.TestCase):

    def test_part_one(self):

        day_six = DaySix()

        self.assertEqual(day_six.part_one(), 6549, "Should be 6549")
        self.assertEqual(day_six.part_two(), 3466, "Should be 3466")


if __name__ == '__main__':
    unittest.main()
