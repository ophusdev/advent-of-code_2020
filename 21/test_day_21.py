import unittest
from day_21 import DayTwentyOne


class TestDayTwentyOne(unittest.TestCase):

    def test_part_one(self):

        day = DayTwentyOne()

        self.assertEqual(day.part_one(), 1977, "Should be 1977")
        self.assertEqual(day.part_two(), "dpkvsdk,xmmpt,cxjqxbt,drbq,zmzq,mnrjrf,kjgl,rkcpxs", "Should be dpkvsdk,xmmpt,cxjqxbt,drbq,zmzq,mnrjrf,kjgl,rkcpxs")


if __name__ == '__main__':
    unittest.main()
