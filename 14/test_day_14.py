import unittest
from day_14 import DayFourthheen


class TestDayThirtheen(unittest.TestCase):

    def test_part_one(self):

        day = DayFourthheen()

        self.assertEqual(day.part_one(), 12408060320841, "Should be 12408060320841")
        self.assertEqual(day.part_two(), 4466434626828, "Should be 4466434626828")


if __name__ == '__main__':
    unittest.main()
