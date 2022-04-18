import unittest
from dates import dates

class TestDates (unittest.TestCase):
    def test_dates(self):
        self.assertEquals('2022-04-18', dates())

if __name__ == "__main__":
    unittest.main()