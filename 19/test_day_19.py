import unittest
from day_19 import DayNineteen


class TestDayNineteen(unittest.TestCase):

    def test_part_one(self):

        day = DayNineteen()

<<<<<<< HEAD
        self.assertEqual(day.part_one(), 3348222486398, "Should be 3348222486398")
        self.assertEqual(day.part_two(), 43423343619505, "Should be 43423343619505")
=======
        self.assertEqual(day.part_one(), 265, "Should be 265")
        self.assertEqual(day.part_two(), None, "Should be None")
>>>>>>> 1e1cf6288a01db1fe9150c69bbf3aed35f5a7ea9


if __name__ == '__main__':
    unittest.main()
