import unittest
from weekdays import month_week_days

class TestWeekDays (unittest.TestCase):
    def test_week_days(self):
        self.assertEquals(21, month_week_days())

if __name__ == "__main__":
    unittest.main()